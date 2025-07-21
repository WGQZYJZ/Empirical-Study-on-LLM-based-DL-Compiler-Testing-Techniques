'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input_data = torch.randn(1)
print(input_data)
output = torch.exp2(input_data)
print(output)