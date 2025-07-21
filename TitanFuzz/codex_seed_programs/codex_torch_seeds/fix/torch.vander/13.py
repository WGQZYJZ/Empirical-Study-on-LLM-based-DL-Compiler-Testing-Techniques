'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(1, 5)
print(x)
print(torch.vander(x, increasing=True))
print(torch.vander(x, increasing=False))
print(torch.vander(x, increasing=True, N=3))
print(torch.vander(x, increasing=False, N=3))