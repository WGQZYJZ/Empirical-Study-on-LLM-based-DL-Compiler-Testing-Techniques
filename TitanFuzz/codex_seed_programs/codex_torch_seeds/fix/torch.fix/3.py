'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
print('Input: ', input)
output = torch.fix(input)
print('Output: ', output)