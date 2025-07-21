'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output = torch.log2(input_data)
print(output)