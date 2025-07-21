'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
import torch
mat1 = torch.rand((4, 3, 2))
mat2 = torch.rand((4, 2, 3))
torch.bmm(mat1, mat2)