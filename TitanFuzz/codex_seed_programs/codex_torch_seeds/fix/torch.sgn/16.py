'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
sgn_output = torch.sgn(input)
print('Output of torch.sgn: ', sgn_output)