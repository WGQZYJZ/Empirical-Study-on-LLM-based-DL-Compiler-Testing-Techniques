'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input1 = torch.rand(2, 3, 4)
output = torch.digamma(input1)
print('Output: ', output)