'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.5, 1, 2])
output_data = torch.arccosh(input_data)
print('Input:', input_data)
print('Output:', output_data)