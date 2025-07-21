'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
output = torch.special.gammaln(input)
print('Input: ', input)
print('Output: ', output)