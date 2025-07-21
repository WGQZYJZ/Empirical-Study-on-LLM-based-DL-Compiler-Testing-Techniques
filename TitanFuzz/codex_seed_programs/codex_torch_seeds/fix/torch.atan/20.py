'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output = torch.atan(input_data)
print(output)
output = torch.atan_(input_data)
print(output)