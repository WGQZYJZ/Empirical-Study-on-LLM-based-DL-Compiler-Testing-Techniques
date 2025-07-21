'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 1)
print('Input data:', input_data)
output_data = torch.frexp(input_data)
print('Output data:', output_data)