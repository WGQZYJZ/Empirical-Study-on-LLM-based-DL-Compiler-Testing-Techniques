'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input: ', input)
output = torch.special.logsumexp(input, dim=1, keepdim=False)
print('Output: ', output)