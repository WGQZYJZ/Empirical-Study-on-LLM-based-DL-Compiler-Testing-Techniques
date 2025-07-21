'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
x = torch.randn(1, 2)
torch.seed()
print(x)
print(torch.randn(1, 2))