'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
input1 = torch.randn(4, 4)
input2 = torch.randn(4, 4)
print('input1: ', input1)
print('input2: ', input2)
output = torch.special.zeta(input1, input2)
print('output: ', output)