'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
input_data = torch.rand(1)
output_data = torch.arcsin(input_data)
print(input_data)
print(output_data)