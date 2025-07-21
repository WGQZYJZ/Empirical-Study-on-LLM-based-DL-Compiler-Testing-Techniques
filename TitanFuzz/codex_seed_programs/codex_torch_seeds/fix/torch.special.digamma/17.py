'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input_data = torch.randn(3)
print(input_data)
output_data = torch.special.digamma(input_data)
print(output_data)