'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
output = torch.rsqrt(input_data)
print(output)