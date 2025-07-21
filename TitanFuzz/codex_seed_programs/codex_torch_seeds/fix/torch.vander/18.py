'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.tensor([1, 2, 3, 5])
print(torch.vander(x, N=3, increasing=True))
print(torch.vander(x, N=3, increasing=False))
print(torch.vander(x, N=4, increasing=True))
print(torch.vander(x, N=4, increasing=False))
print(torch.vander(x, N=5, increasing=True))
print(torch.vander(x, N=5, increasing=False))