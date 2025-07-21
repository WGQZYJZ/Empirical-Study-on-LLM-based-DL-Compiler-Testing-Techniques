'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(4, 5)
c = torch.rand(6, 7)
d = torch.rand(8, 9)
torch.block_diag(a, b, c, d)