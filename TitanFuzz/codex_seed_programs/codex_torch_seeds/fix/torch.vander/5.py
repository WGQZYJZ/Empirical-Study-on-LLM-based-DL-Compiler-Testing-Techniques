'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(1, 5)
print(x)
y = torch.vander(x, 3, True)
print(y)