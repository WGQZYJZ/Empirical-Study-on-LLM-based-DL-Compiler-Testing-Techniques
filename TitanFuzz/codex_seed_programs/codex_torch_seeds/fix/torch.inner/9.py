'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
input = torch.rand(4, 3)
other = torch.rand(3)
print('Input:', input)
print('Other:', other)
result = torch.inner(input, other)
print('Result:', result)