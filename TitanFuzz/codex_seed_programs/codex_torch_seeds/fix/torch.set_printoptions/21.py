'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = torch.randn(3, 3)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=2, profile=None, sci_mode=None)
print('x = ', x)
print('y = ', y)
print('z = ', z)