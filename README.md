# FracXAI - An Explainable Vision-Language Clinical Decision Support Tool for Bone Fracture Diagnosis

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.14.0-red.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-FF4B4B.svg)](https://streamlit.io/)
[![MedGemma](https://img.shields.io/badge/Model-MedGemma--4B-4285F4.svg)](https://huggingface.co/google/medgemma-4b-it)

A medical AI diagnostic tool that fine-tunes Google's MedGemma vision-language model to detect and classify bone fractures from radiographs, paired with GradCAM visual explanations so clinicians can see which regions of an X-ray drove each prediction.

> **Research prototype only not validated for clinical use.**


## Important: Notebooks Folder
**The `notebooks/` folder contains the standalone experimental workflow used during development.** They can be used to review individual parts of the project without running the full app.

**Used in the final project:**
- `notebooks/Medgemma_Mendeley_finetuned.ipynb` — Mendeley fracture-subtype fine-tuning



## Quick Start

### Prerequisites

- Python 3.10 or higher
- NVIDIA GPU strongly recommended (developed and tested on Google Colab, A100 GPU) — local CPU/MPS inference was found to be impractically slow for a 4B-parameter model
- A Hugging Face account with access to `google/medgemma-4b-it` 

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AdelabuAderonke/FracXAI.git
cd FracXAI
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up authentication**
```bash
huggingface-cli login
# paste your Hugging Face access token when prompted
```

5. **Download the fine-tuned model adapters**
Model weights are hosted on Google Drive (not included in this repository due to file size — see [Model Weights](#model-weights) below) and should be placed in a local `models/` folder matching the paths in `app/config.py`, or accessed directly via Drive if running in Colab.

### Running the Application

**Option 1:** Streamlit directly
```bash
streamlit run app/main.py
```

**Option 2:** On Google Colab (recommended, given hardware requirements)
```python
!git clone https://github.com/AdelabuAderonke/FracXAI.git
%cd FracXAI
!pip install -r requirements.txt

from google.colab import userdata
import os
os.environ["HF_TOKEN"] = userdata.get("HF_TOKEN")

!nohup streamlit run app/main.py --server.port 8501 > /content/logs.txt 2>&1 &

from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_TOKEN")
print(ngrok.connect(8501))
```

Navigate to the printed URL (or `http://localhost:8501` if running locally).

## Project Structure



## Step-by-Step User Guide

### Step 1: Choose a Task

When you launch the application, select the task for the model.
<img width="1413" height="642" alt="first_step" src="https://github.com/user-attachments/assets/5a27b62a-78dd-4b18-95bd-42800afc4a99" />


**Choose your task:**
- **Classify fracture type** — assumes a fracture is already present, and identifies it as simple or comminuted

**What Happens:**
- The interface displays a scope disclaimer relevant to the selected task
- The  fine-tuned LoRA adapter is loaded

---

### Step 2: Upload an X-ray

<img width="1352" height="488" alt="second_step" src="https://github.com/user-attachments/assets/52f76b96-8717-4715-9e42-7e3ccd8e4565" />


**What Happens:**
- The image is displayed for confirmation before analysis
- No image is stored beyond the active session

---

### Step 3: Run Analysis

<img width="1427" height="537" alt="third_step" src="https://github.com/user-attachments/assets/bcb9e0ac-c2f2-4cdd-9a1b-d9e16e6d5a0d" />

**What Happens:**
- The selected model generates a natural-language diagnostic description
- The response is parsed into a clear result (e.g. "Fracture present")

---

### Step 4: Review the GradCAM Explanation

<img width="1376" height="732" alt="fourth_step" src="https://github.com/user-attachments/assets/eadd1762-200b-414a-ae21-313d85460e6f" />


**What Happens:**
- A heatmap overlay highlights the image regions that most influenced the model's diagnosis
- Warmer regions indicate greater influence on the generated result

## Model Performance Summary

| Model | Task | Accuracy (fine-tuned) | Accuracy (base MedGemma) |
|---|---|---|---|
| Model  | Fracture subtype classification | 90.0% | 45.7% |


Full methodology, evaluation metrics, and confusion matrices are documented in the accompanying project report.

## Model Weights

Fine-tuned adapter weights (~2.8GB each) are hosted on Google Drive rather than in this repository, due to file size:

- Fine-tuned  Model  (fracture subtype): *(https://drive.google.com/drive/folders/1UuSwpTNHLnT6Uiva3eu50dQ6T5zBnufE?usp=drive_link)*

Each folder is shared as "Anyone with the link — Viewer". Download the relevant folder(s) and place them under a local `models/` directory matching the paths configured in `app/config.py`, or mount your own copy of Google Drive and update `config.py`'s paths accordingly if running in Colab.

## Datasets

- **[Mendeley Bone Fracture Dataset](https://data.mendeley.com/datasets/8d9kn57pdj/1)** — The original folder contains 2,384 images, categorised as simple or comminuted fractures

Datasets are publicly available and de-identified; no primary data collection was undertaken as part of this project.

## Limitations

- Training responses were template-generated from structured labels, not authored by radiologists
- GradCAM explanations have not been independently validated against expert-annotated regions of clinical significance

## Acknowledgments

- **Google**: for the MedGemma model family
- **Talha et al.(2024)**: for Mendeley dataset
- **Hugging Face**: for `transformers`, `peft`, and `trl`
- **Streamlit**: for the application framework

## Contributor

- **Aderonke Adelabu**

**Supervisor: Dr. Olamilekan Shobayo**
