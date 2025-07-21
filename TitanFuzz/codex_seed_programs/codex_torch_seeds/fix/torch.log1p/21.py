'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
output = torch.log1p(input_data)
print(output)