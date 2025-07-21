'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 2)
print(input_data)
output_data = torch.cosh(input_data)
print(output_data)