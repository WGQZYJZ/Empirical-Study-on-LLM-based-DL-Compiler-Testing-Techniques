'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
output_data = torch.reciprocal(input_data)
print(output_data)