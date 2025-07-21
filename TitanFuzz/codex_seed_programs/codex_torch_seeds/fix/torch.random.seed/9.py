'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
x = torch.randn(2, 2)
print(x)
torch.random.seed()
x = torch.randn(2, 2)
print(x)