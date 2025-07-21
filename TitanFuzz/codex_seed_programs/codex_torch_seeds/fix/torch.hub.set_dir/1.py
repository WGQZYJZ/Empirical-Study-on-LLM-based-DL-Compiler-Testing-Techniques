'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.set_dir\ntorch.hub.set_dir(d)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 3, 224, 224)
torch.hub.set_dir('/tmp/my_cache_dir')
model = torch.hub.load('pytorch/vision:v0.5.0', 'resnet18', pretrained=True)
model.eval()
output = model(input_data)
print(output.shape)