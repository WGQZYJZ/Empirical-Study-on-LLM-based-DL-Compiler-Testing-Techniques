'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
output = torch.multiply(input_data, input_data)
print(output)