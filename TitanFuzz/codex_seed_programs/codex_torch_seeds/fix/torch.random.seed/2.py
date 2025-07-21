'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
x = torch.randn(5, 5)
y = torch.randn(5, 5)
torch.random.seed()
print(x)
print(y)