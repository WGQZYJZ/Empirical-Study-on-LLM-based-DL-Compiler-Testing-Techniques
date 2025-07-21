'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 3, 3)
model = nn.Sequential(nn.Conv2d(1, 1, 3, 1, 1), nn.ReLU(), nn.Conv2d(1, 1, 3, 1, 1), nn.ReLU())
output_data = model(input_data)
print(output_data)