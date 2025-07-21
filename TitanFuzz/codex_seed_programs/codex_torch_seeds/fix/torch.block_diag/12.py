'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
a = torch.randn(3, 3)
b = torch.randn(3, 3)
c = torch.randn(3, 3)
torch.block_diag(a, b, c)