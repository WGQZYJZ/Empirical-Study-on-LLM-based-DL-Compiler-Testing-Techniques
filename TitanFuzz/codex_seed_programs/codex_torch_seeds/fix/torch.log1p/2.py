'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
input_data = torch.randn(10)
print(input_data)
output_data = torch.log1p(input_data)
print(output_data)