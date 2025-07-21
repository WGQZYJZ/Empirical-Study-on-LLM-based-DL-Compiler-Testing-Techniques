'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
torch.set_printoptions(precision=8)
a = torch.randn(3, 3)
b = torch.randn(3, 1)
c = (a * b)
print(c)