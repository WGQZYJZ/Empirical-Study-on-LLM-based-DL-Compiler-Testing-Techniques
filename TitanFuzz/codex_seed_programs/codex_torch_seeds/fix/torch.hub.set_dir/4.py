'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.set_dir\ntorch.hub.set_dir(d)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.hub import load_state_dict_from_url
torch.hub.set_dir('/tmp/torch_hub')
input = torch.randn(1, 3, 224, 224)
model = torch.hub.load('pytorch/vision:v0.5.0', 'alexnet', pretrained=True)
model.eval()
torch.hub.set_dir('/tmp/torch_hub')
model = torch.hub.load('pytorch/vision:v0.5.0', 'alexnet', pretrained=True)
model.eval()
output = model(input)
print(output.shape)