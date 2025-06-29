[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb)

# AI-Story-Generator
AI Story Generator is a web app that generates creative short stories from user prompts using the DeepSeek Coder 6.7B-Instruct model, with a clean Gradio interface.

This is an AI-powered creative story generator built using the DeepSeek Coder model and Gradio interface.


## :link:Features

- Generate creative short stories based on your prompts
- Custom-styled Gradio interface
- Built with Transformers, Accelerate, and BitsAndBytes


## :link:Try It in Google Colab

Click the badge below to run the notebook directly in Google Colab:

[https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb](https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb)

Before Running the Code we should set Runtime from CPU to T4-GPU and then start running the Code in the Colab.

## :link:Screenshots

<b>1. We will get an interface like this. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/1.png)

<b>2. We can give a Prompt to Generate Story. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/2.png)

<b>3. As Shown in the image below it will generate a story. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/3.png)

<b>4. This is the final output after it generating story.</b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/4.png)

## :link:Installation: To run locally

 cloning the Repo in VS Code Terminal:
 ```bash
     git clone https://github.com/pranay2686/Ai-Story-Generator.git
```
To Run Locally in VS Code use app.py and requirements.txt files that i shared.

For Creating Folder
 ```bash
 cd Ai-Story-Generator
```
This Command below is to Create Virtual Environment:
  ```bash
  python -m venv venv
```
This Command in the below is to Activate Virtual Environment:
 ```bash
 venv\Scripts\activate (on Windows) or source venv/bin/activate (on Mac or Linux)
```
The below command is to install All dependencies in the requirements.txt:
```bash
  pip install -r requirements.txt
```
To run the code finally use the below command:
```bash
  python app.py
```

## :link:Note:
In my opinion, I would not suggest running this code locally using VS Code, especially if you're using a CPU. This is because the DeepSeek model we're using is quite large, and generating output on a CPU can take a very long time. Instead, I recommend using the Google Colab link I’ve provided. Colab uses a T4 GPU, which significantly speeds up the execution and provides faster and more accurate results.

## :link:Important Notes for Local Use

This notebook uses the `deepseek-ai/deepseek-coder-6.7b-instruct` model, which:

- Requires a GPU with **at least 10 GB VRAM** (e.g. NVIDIA T4, V100, A100)
- **Will not work** on most CPUs because it uses bitsandbytes GPU quantization
- May run **extremely slowly or crash** if attempted on CPU
- For best performance, we recommend:
  - Running in **Google Colab** with GPU enabled
  - Using a local machine with a **CUDA-enabled GPU**

If your laptop or desktop has a compatible NVIDIA GPU, you may also try running the notebook locally. Otherwise, Colab is the easiest way to run this project.

**Note:** Free Colab accounts may have limited GPU quotas.




