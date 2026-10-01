# Base model
BASE_MODEL_ID = "google/medgemma-4b-it"

# Fine-tuned adapter paths 
MODEL_A_PATH = "/content/drive/MyDrive/Dissertation/models/medgemma-4b-it-sft-lora-mendeley-final"

# Model A: fracture subtype classification
PROMPT_A = (
    "What type of bone fracture is shown in this X-ray?\n"
    "A: simple fracture\n"
    "B: comminuted fracture"
)
FRACTURE_CLASSES_A = ["A: simple fracture", "B: comminuted fracture"]



# App text
APP_TITLE = "FracXAI"
APP_SUBTITLE = "AI bone fracture detection with Grad-CAM explainability"
RESEARCH_DISCLAIMER = "Research demo — not for clinical use"
SCOPE_DISCLAIMER = (
    "Research demo — not for clinical use"
)