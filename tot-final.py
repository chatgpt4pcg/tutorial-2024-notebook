class TreeOfThoughtPrompting(TrialLoop):
    @staticmethod
    def extract_scores(scores_str: str):
        import re
        scores_str = scores_str.lower()
        stability_pattern = r".*stability: (10|\d).*"
        similarity_pattern = r".*similarity: (10|\d).*"
        stability = 0
        similarity = 0
        if stability_match := re.search(stability_pattern, scores_str):
            stability = int(stability_match.group(1))
        if similarity_match := re.search(similarity_pattern, scores_str):
            similarity = int(similarity_match.group(1))
        return stability, similarity

    @staticmethod
    def tot(ctx: TrialContext, target_character: str) -> str:
        max_depth = 2
        branching_factor = 2

        current_content = ""

        task_prompt_template = open(Path("prompts/task-tot.txt"), "r").read()
        evaluation_prompt_template = open(Path("prompts/evaluate-tot.txt"), "r").read()
        answer_prompt_template = open(Path("prompts/answer-tot.txt"), "r").read()

        try:
            # Loop until reaching the maximum depth
            for i in range(max_depth):
                # | 1. Perform the task to generate {branching_factor} thoughts
                responses = []

                for j in range(branching_factor):
                    res = chat_with_llm(ctx, [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": task_prompt_template.format(
                            object=target_character,
                            generated_content_so_far=current_content == "" and "nothing" or current_content,
                        )}])
                    responses.append(res[0])

                # | 2.1. Evaluate each thought ...
                scores = []
                for response in responses:
                    score = chat_with_llm(ctx, [
                        {"role": "user", "content": evaluation_prompt_template.format(
                            object=target_character,
                            generated_content_so_far=f"{current_content}\n{response}"
                        )}])[0]

                    evaluation_result = (response, TreeOfThoughtPrompting.extract_scores(score))
                    scores.append(evaluation_result)

                # | 2.2. ... and select the best one
                best_performing_thought = sorted(scores, key=lambda x: sum(x[1]), reverse=True)
                current_content += f"{best_performing_thought[0][0]}\n"

            # | 3. Repeat the process with the selected thought

            # Format the final response in a correct format and return it
            final_response = chat_with_llm(ctx, [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": answer_prompt_template.format(
                    generated_content=current_content
                )}
            ])

            return final_response[0]
        except (ValueError, TimeoutError) as e:
            print(e)
            return current_content

    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        """
        Runs the tree-of-thought prompting.
        :param ctx: The trial context.
        :param target_character: The target character.
        :return: The generated text.
        """
        final_response = TreeOfThoughtPrompting.tot(ctx, target_character)

        return final_response