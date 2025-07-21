'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print(input_data)
output = torch.deg2rad(input_data)
print(output)