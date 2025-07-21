'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
torch.set_printoptions(precision=2, threshold=2, edgeitems=2, linewidth=2, profile=2, sci_mode=2)
print(a)