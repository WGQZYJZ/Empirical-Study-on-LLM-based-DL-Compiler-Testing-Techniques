'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input = torch.rand(3, 4)
other = torch.rand(3, 4)
output = torch.less(input, other)
print('Output: ', output)