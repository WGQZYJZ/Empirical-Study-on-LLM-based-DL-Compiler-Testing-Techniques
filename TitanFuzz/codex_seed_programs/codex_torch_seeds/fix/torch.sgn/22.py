'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
output = torch.sgn(input_data)
print('Input data:', input_data)
print('Output:', output)