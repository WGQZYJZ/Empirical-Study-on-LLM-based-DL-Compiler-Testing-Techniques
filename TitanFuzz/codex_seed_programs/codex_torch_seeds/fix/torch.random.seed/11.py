'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
x = torch.rand(3, 3)
torch.random.seed()
print(x)
y = torch.rand(3, 3)
print(y)
torch.random.seed()
print(y)
z = torch.rand(3, 3)
print(z)