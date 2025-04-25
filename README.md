# 🧠 SmartScanGPT

SmartScanGPT is a full-stack AI agent that accepts handwritten technical scans, performs OCR, and generates CEO-grade deep-tech whitepapers using the DeepSeek 7B model — fully offline and open-source.

---

## 🚀 Use Case

Designed for deep-tech ventures like BioMetallica, SmartScanGPT turns technical notes, lab reports, and strategy outlines into formal R&D briefings suitable for:

- Investor presentations
- Grant applications
- Internal alignment
- Technical due diligence

---

## 🧠 What It Does

1. **📤 Upload** a handwritten scan/image (`.png`, `.jpg`, `.pdf`, etc.)
2. **👁️ OCR** runs on-device using EasyOCR to extract raw text
3. **🧩 Injects** domain-specific static context for prompt control
4. **🤖 Generates** a modular, strategic technical report using DeepSeek 7B
5. **📄 Displays** report in a scrollable, editable UI

---

## 🛠️ Tech Stack

| Component      | Tool / Library                     |
|----------------|------------------------------------|
| Frontend       | Streamlit                          |
| OCR Engine     | EasyOCR                            |
| Image Handling | Pillow (`PIL`)                     |
| LLM Backend    | `deepseek-ai/deepseek-llm-7b-chat` |
| LLM Runtime    | PyTorch, Transformers              |
| Prompt Engine  | Static context injection           |

---

## 🖼️ Sample Flow

1. Upload scan  
2. OCR: `"Metal separation rate exceeded baseline threshold"`  
3. Static prompt + extracted text →  
4. Output:

> *“Our decentralized bioreactor platform demonstrates modular viability for low-grade e-waste recovery. Current TRL assessments indicate pilot readiness (TRL 6) across microbial control and sensor feedback integration…”*

---

## 💻 Local Setup

### 1. Clone and Install
```bash
git clone https://github.com/your-org/SmartScanGPT.git
cd SmartScanGPT
pip install -r requirements.txt

### 2. Run the App
streamlit run app.py
Requires 16GB+ RAM or GPU (T4/A10/A100 recommended for DeepSeek)