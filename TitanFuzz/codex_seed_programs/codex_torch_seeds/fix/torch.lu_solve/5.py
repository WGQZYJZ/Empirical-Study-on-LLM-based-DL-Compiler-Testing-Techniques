'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lu_solve\ntorch.lu_solve(b, LU_data, LU_pivots, *, out=None)\n'
import torch
A = torch.rand(3, 3, dtype=torch.float64)
b = torch.rand(3, 1, dtype=torch.float64)
(LU_data, LU_pivots) = torch.lu(A)
x = torch.lu_solve(b, LU_data, LU_pivots)
print('A:\n', A)
print('b:\n', b)
print('x:\n', x)
print('Ax:\n', A.mm(x))