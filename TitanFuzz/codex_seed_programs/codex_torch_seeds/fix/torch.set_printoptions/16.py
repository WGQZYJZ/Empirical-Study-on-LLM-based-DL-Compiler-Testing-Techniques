'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
torch.set_printoptions(precision=1, threshold=1, edgeitems=2, linewidth=80, profile='full', sci_mode=False)
print(x)
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)
print(x)