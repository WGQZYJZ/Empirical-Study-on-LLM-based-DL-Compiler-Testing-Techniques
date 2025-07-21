'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nextafter\ntorch.nextafter(input, other, *, out=None)\n'
import torch
input = torch.randn(4)
other = torch.randn(4)
out = torch.nextafter(input, other)
print('Input: ', input)
print('Other: ', other)
print('Output: ', out)
out = torch.nextafter(input, other, out=torch.empty_like(input))
print('Output: ', out)