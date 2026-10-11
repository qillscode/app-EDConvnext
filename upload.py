from huggingface_hub import login, HfApi

login()

api = HfApi()

api.upload_file(
    path_or_fileobj="convnext_ferplus_statedict.pth",
    path_in_repo="convnext_ferplus_statedict.pth",
    repo_id="qillscode/convnext-ferplus",
    repo_type="model"
)