'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 3)
flatten = nn.Flatten()
output_data = flatten(input_data)
print(input_data)
print(output_data)