'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
x = torch.rand(3, 4)
torch.unbind(x, dim=0)
torch.unbind(x, dim=1)