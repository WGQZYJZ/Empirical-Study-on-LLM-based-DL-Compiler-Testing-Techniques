'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
print('input: ', input)
print('other: ', other)
print('input < other: ', torch.less(input, other))
print('input < 0.5: ', torch.less(input, 0.5))
print('input < 0.5: ', torch.less(input, torch.tensor(0.5)))