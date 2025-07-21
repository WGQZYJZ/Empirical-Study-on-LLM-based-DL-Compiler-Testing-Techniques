'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input1 = torch.randn(3, 3)
input2 = torch.randn(3, 3)
output = torch.hypot(input1, input2)
print('input1: ', input1)
print('input2: ', input2)
print('output: ', output)