from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

model_name = "deepseek-ai/deepseek-coder-6.7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_story(prompt):
    if not prompt.strip():
        return " Please enter a story prompt!"

    story_prompt = (
        "Write a creative short story based on the following prompt. "
        "The story should include:\n"
        "- An engaging beginning\n"
        "- Interesting characters\n"
        "- A conflict or challenge\n"
        "- A satisfying resolution\n\n"
        f"Prompt: {prompt}\n\nStory:"
    )

    try:
        inputs = tokenizer(story_prompt, return_tensors="pt").to("cpu")
        outputs = model.generate(**inputs, max_new_tokens=500)
        story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if "Story:" in story:
            story = story.split("Story:")[1].strip()
        return story
    except Exception as e:
        return f" Error: {str(e)}"

custom_css = """
body {
    background: #fdfdfd;
    font-family: 'Segoe UI', sans-serif;
    color: #1f2937;
}

.gr-markdown h1 {
    font-size: 36px;
    color: #3b0764;
    text-align: center;
    margin-top: 20px;
}

.gr-textbox textarea {
    font-size: 16px !important;
    font-family: 'Georgia', serif !important;
    border-radius: 12px !important;
    background: #fff9f0 !important;
    border: 2px solid #fde68a !important;
    padding: 14px !important;
    resize: vertical;
}

.gr-button {
    background: linear-gradient(to right, #f59e0b, #eab308) !important;
    color: #1f2937 !important;
    font-weight: 600;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 10px;
    margin-top: 10px;
}

.gr-button:hover {
    background: #facc15 !important;
}

#story-card {
    background: #1e1e1e;
    border-left: 6px solid #fbbf24;
    padding: 20px;
    margin-top: 20px;
    font-size: 16px;
    border-radius: 10px;
    font-family: 'Georgia', serif;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    color: #3f6212;
    white-space: pre-wrap;
}

@media (max-width: 600px) {
    .gr-textbox textarea, #story-card {
        font-size: 15px !important;
    }
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Base()) as demo:
    gr.Markdown("# AI Story Generator")

    prompt_input = gr.Textbox(
        label=" Enter a creative story prompt:",
        placeholder="e.g., A dragon discovers an abandoned library in the mountains...",
        lines=4,
    )

    generate_btn = gr.Button(" Tell me a story")

    story_output = gr.Textbox(
        label=" Your AI Story",
        interactive=False,
        lines=20,
        elem_id="story-card",
        show_copy_button=True
    )

    gr.Examples(
        examples=[
            ["A girl finds a door behind her wardrobe that leads to another century"],
            ["An alien becomes friends with a stray dog in New York"],
            ["A village where people dream the same dream every night"],
        ],
        inputs=prompt_input
    )

    generate_btn.click(fn=generate_story, inputs=prompt_input, outputs=story_output)

demo.launch()
