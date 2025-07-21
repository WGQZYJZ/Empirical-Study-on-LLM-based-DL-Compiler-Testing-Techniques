'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
import torch.nn as nn
input_data = torch.randn(10, 3)
model = nn.Sequential(nn.Linear(3, 4), nn.ReLU(), nn.Linear(4, 1))
output = model(input_data)
print(output)