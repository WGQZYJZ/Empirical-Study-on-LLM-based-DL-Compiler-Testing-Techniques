'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triangular_solve\ntorch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
A = torch.rand(3, 3)
b = torch.rand(3, 2)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)[0]
print('A:', A)
print('b:', b)
print('x:', x)