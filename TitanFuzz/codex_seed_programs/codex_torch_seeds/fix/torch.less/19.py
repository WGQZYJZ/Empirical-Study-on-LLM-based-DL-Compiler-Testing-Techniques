'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 2)
other = torch.randn(2, 2)
output = torch.less(input, other)
print('output:', output)
print('output.dtype:', output.dtype)
print('output.size():', output.size())
'\noutput: tensor([[False,  True],\n                [False, False]])\noutput.dtype: torch.bool\noutput.size(): torch.Size([2, 2])\n'