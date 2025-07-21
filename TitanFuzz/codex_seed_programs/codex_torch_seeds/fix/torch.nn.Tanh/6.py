'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, requires_grad=True)
model = nn.Tanh()
output = model(input_data)
print(output)