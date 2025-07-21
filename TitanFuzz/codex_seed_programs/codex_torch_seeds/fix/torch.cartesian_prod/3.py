'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
x = torch.arange(1, 4)
y = torch.arange(1, 3)
z = torch.arange(1, 5)
torch.cartesian_prod(x, y, z)