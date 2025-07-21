'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input data: ', input)
output = torch.special.i0e(input)
print('Output data: ', output)