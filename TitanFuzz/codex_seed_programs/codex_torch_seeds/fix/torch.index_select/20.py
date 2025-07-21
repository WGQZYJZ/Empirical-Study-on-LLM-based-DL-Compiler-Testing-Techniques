'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
x = torch.randn(4, 5)
torch.index_select(x, 0, torch.tensor([0, 3]))
torch.index_select(x, 1, torch.tensor([0, 3]))