'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
a = torch.rand(4, 4)
b = a.view(16)
c = a.view((- 1), 8)
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)
print(a)
print(b)
print(c)