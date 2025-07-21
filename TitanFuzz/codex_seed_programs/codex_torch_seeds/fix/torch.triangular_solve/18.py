'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triangular_solve\ntorch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
A = torch.randn(3, 3)
b = torch.randn(3, 4)
x = torch.triangular_solve(b, A, upper=False)[0]
print(x)
print(torch.matmul(A, x))