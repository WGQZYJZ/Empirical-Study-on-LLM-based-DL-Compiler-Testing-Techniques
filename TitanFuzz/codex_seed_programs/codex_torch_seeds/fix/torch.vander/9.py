'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(1, 4, dtype=torch.float)
y = torch.vander(x, 2, False)
print(y)