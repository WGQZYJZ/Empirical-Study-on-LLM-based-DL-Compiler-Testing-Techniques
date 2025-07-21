'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
output = torch.neg(input)
print('input:\n', input)
print('output:\n', output)