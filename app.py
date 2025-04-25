import streamlit as st
import easyocr
from PIL import Image
import openai
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-llm-7b-chat")
    model = AutoModelForCausalLM.from_pretrained(
        "deepseek-ai/deepseek-llm-7b-chat",
        torch_dtype=torch.float32,
        device_map="auto",
        offload_folder = "./offload"
    )
    return tokenizer, model

tokenizer, model = load_model()
with open("static_prompt.txt", "r") as f:
    STATIC_PROMPT = f.read()

uploaded_file = st.file_uploader("Upload Image", type =["png", "jpg", "jpeg", "GIF", "TIFF", "BMP", "PDF"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Here's your uploaded image!", use_column_width=True)
    reader = easyocr.Reader(['en'])
    with st.spinner("Reading your handwriting.."):
        result = reader.readtext(image)
        extracted_text = "\n".join([entry[1] for entry in result])
        st.success("Done Reading")
    st.text_area("Extracted Text:", extracted_text, height = 200)
    final_prompt = STATIC_PROMPT + "\n\n" + extracted_text
    if st.button("Generate Report"):
        with st.spinner("Thinking very hard..."):
            prompt = f"<|user|>\n{final_prompt}\n <|assistant|>"
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                top_p=0.95
            )
            decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
            generated_text = decoded.split("<|assistant|>")[-1].strip()
        st.success("Report Ready!")
        st.text_area("Generated Report", generated_text, height=400)






