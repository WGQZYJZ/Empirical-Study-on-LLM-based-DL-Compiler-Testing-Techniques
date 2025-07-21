'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.randn(4, 4)
torch.row_stack((a, b))
torch.row_stack((a, b, c))