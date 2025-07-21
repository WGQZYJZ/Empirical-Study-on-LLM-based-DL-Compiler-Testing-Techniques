'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load_state_dict_from_url\ntorch.hub.load_state_dict_from_url(url, model_dir=None, map_location=None, progress=True, check_hash=False, file_name=None)\n'
import torch
x = torch.randn(1, 3, 224, 224)
model = torch.hub.load_state_dict_from_url('https://download.pytorch.org/models/resnet50-19c8e357.pth', progress=True)
print(model)