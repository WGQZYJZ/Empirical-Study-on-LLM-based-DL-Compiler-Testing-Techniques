'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
output_data = torch.expm1(input_data)
print(output_data)