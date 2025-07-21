'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.randn(100)
output = torch.arccos(input_data)
print('Input:', input_data)
print('Output:', output)