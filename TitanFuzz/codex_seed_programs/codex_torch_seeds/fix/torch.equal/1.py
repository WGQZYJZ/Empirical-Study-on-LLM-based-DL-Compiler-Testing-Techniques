'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.equal(x, y)
print('z = ', z)