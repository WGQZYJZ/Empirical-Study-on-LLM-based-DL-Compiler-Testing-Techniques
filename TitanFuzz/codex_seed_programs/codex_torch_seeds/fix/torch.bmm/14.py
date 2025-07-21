'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
import torch
input = torch.randn(1, 3, 4)
mat2 = torch.randn(1, 4, 5)
torch.bmm(input, mat2)