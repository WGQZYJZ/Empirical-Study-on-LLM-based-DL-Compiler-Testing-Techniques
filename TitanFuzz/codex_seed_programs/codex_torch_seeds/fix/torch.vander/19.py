'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(4, dtype=torch.float)
print(x)
print(torch.vander(x, increasing=True))
print(torch.vander(x, increasing=False))
print(torch.vander(x, N=3, increasing=True))
print(torch.vander(x, N=3, increasing=False))
print(torch.vander(x, N=4, increasing=True))
print(torch.vander(x, N=4, increasing=False))