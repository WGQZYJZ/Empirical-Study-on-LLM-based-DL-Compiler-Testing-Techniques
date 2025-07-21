'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.tensor([1, 2, 3, 5])
print(torch.vander(x, N=None, increasing=False))