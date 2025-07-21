'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input = torch.randn(3, requires_grad=True)
print('Input: ', input)
output = torch.neg(input)
print('Output: ', output)