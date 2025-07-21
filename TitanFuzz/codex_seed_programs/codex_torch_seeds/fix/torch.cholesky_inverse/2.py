'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
torch.cholesky_inverse(input)
torch.cholesky_inverse(input, upper=True)