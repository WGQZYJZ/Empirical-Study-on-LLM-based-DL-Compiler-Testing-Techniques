'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 1)
print(input_data)
output_data = torch.log2(input_data)
print(output_data)