# Prompt Engineering for Science Birds Level Generation and Beyond Tutorial at IEEE CoG 2024 Tutorial

This repository contains a codebase for the tutorial on prompt engineering for procedural content generation at the IEEE
CoG 2024. The tutorial utilizes [the LLM4PCG Python package](https://github.com/Pittawat2542/llm4pcg-python), which is a
package based on the original [ChatGPT4PCG](https://github.com/chatgpt4pcg/chatgpt4pcg-python) package but is adapted
for supporting open-source/weight OpenAI API-compatible models.

## Installation

To use this codebase, you must have [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
and [Jupyter](https://jupyter.org/install) installed on your
system.

1. Open your terminal or command prompt.

2. Create a new conda environment with Python 3.12:

```
conda create -n cog-tutorial python=3.12
```

3. Activate the newly created environment:

```
conda activate cog-tutorial
```

4. Install Jupyter Lab in the activated environment:

```
conda install -c conda-forge jupyterlab
```

5. Once the installation is complete, you can launch Jupyter Lab by running:

```
jupyter lab
```

# Running the Tutorial

Next, you can run the tutorial notebook by following the instructions below.

1. Clone this repository to your local machine.

```
git clone https://github.com/chatgpt4pcg/tutorial-2024-notebook.git
```

2. Change directory to the cloned repository:

```
cd tutorial-2024-notebook
```

3. Open the notebook `tutorial.ipynb` in Jupyter by navigating to the cloned repository in Jupyter Lab and clicking on
   the notebook file.

## Contributing

If you would like to contribute to this project, please fork this repository and submit a pull request. Please ensure
that your code is well documented and that you have tested your code before submitting a pull request.
