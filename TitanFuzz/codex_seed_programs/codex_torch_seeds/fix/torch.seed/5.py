'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
print(x)
print(y)
torch.seed()
print(torch.equal(x, y))
torch.seed()
x = torch.rand(2, 3)
y = torch.rand(2, 3)
print(torch.equal(x, y))