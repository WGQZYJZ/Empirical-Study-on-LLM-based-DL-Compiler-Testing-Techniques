'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print(input_data)
output_data = torch.arccos(input_data)
print(output_data)