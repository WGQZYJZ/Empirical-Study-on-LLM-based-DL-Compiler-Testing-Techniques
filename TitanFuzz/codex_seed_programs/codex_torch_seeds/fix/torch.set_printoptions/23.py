'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.rand(2, 3)
print(x)
torch.set_printoptions(precision=5, threshold=5, edgeitems=5, linewidth=5, profile=None, sci_mode=None)
print(x)
torch.set_printoptions(profile='default')
print(x)