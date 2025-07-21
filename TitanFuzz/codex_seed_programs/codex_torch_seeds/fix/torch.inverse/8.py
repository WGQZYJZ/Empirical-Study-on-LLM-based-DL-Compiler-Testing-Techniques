'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
A = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
A_inv = torch.inverse(A)
print('A: ', A)
print('A_inv: ', A_inv)