'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('input:', input)
output = torch.neg(input)
print('output:', output)