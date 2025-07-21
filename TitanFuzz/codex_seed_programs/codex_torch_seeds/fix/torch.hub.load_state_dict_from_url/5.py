'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load_state_dict_from_url\ntorch.hub.load_state_dict_from_url(url, model_dir=None, map_location=None, progress=True, check_hash=False, file_name=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
torch.hub.load_state_dict_from_url('https://download.pytorch.org/models/resnet18-5c106cde.pth')