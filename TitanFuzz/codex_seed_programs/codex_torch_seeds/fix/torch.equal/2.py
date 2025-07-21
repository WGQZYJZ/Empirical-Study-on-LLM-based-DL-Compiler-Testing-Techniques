'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x = torch.rand(1, 3)
y = torch.rand(1, 3)
print(torch.equal(x, y))