'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 3)
print('input1: ', input1)
print('input2: ', input2)
output = torch.cat((input1, input2), 0)
print('output: ', output)