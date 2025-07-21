'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2)
print(input_data)
output_data = torch.lgamma(input_data)
print(output_data)