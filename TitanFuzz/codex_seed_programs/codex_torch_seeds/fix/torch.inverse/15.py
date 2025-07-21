'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
A = torch.randn(3, 3)
A
A_inv = torch.inverse(A)
A_inv
torch.mm(A, A_inv)
torch.mm(A_inv, A)