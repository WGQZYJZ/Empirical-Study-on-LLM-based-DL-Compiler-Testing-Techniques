'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float64)
print('Input: ', input)
print('Gammaln: ', torch.special.gammaln(input))