'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
x = torch.tensor([(- 3.1415), 3.1415])
y = torch.tensor([2.7183])
z = torch.remainder(x, y)
print('The remainder of x / y: ', z)