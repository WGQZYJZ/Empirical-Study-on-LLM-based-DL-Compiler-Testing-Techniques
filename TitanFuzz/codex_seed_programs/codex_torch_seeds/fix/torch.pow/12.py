'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
exponent = torch.tensor([2, 3, 4])
output_data = torch.pow(input_data, exponent)
print(output_data)