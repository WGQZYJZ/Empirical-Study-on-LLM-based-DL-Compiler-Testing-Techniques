'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.randn(5, 3)
y = torch.randn(5, 2)
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)
print(x)
print(y)