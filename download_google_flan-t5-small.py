from huggingface_hub import snapshot_download

MODEL_ID = "google/flan-t5-small"   # change to any model you want
LOCAL_DIR = "./models/flan_t5_small"

snapshot_download(
    repo_id=MODEL_ID,
    local_dir=LOCAL_DIR,
    local_dir_use_symlinks=False,
    ignore_patterns=["*.bin"],  # force SafeTensors if available
)

print("Model downloaded to:", LOCAL_DIR)
