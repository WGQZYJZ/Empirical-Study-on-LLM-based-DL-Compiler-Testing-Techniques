'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.rand(3, 4)
print(x)
torch.set_printoptions(precision=3)
print(x)
torch.set_printoptions(precision=2, threshold=1)
print(x)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2)
print(x)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100)
print(x)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100, profile='full')
print(x)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100, profile='full', sci_mode=False)
print(x)