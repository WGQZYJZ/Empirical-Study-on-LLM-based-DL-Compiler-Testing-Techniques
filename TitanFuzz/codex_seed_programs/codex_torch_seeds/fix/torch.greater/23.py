'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
print(torch.greater(input, other))
'\nTask 4: Call the API torch.greater_equal\ntorch.greater_equal(input, other, *, out=None)\n'
print(torch.greater_equal(input, other))
'\nTask 5: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
print(torch.less(input, other))
'\nTask 6: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
print(torch.less_equal(input, other))