'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
a = torch.rand(3, 4)
print(a)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=False)
print(a)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=True)
print(a)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=False)
print(a)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=True)
print(a)