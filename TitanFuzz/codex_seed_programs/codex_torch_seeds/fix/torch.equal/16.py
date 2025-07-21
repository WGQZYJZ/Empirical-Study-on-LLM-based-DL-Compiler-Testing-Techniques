'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x = torch.ones(3, 3)
y = torch.ones(3, 3)
z = (x == y)
print(z)
print(torch.equal(x, y))