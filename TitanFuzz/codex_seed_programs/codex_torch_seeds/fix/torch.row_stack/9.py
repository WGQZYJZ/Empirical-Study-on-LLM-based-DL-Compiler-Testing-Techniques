'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
torch.row_stack((x, y))