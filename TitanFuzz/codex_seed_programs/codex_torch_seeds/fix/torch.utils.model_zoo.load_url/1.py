'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.model_zoo.load_url\ntorch.utils.model_zoo.load_url(url, model_dir=None, map_location=None, progress=True, check_hash=False, file_name=None)\n'
import torch
input_data = torch.randn(1, 3, 224, 224)
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
model = torch.utils.model_zoo.load_url(url)
print(model)