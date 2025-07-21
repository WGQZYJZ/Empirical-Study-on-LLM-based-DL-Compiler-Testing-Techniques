'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data: ', input_data)
output = torch.reciprocal(input_data)
print('Output: ', output)