'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input = torch.randn(4)
print('Input: ', input)
output = torch.special.gammaln(input)
print('Output: ', output)