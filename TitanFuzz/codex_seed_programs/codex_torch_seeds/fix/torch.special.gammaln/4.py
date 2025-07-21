'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
if True:
    input = torch.randn(2, 3)
    print('Input: ', input)
    print('Output: ', torch.special.gammaln(input))