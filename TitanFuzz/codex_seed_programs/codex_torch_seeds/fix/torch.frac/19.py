'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print(input_data)
output_data = torch.frac(input_data)
print(output_data)