'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('The input data is: ', input)
output = torch.frexp(input)
print('The output data is: ', output)