'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
x = torch.rand(5, 3)
print(x)
torch.random.seed()
y = torch.rand(5, 3)
print(y)