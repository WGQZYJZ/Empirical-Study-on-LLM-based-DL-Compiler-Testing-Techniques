'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lu_solve\ntorch.lu_solve(b, LU_data, LU_pivots, *, out=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
b = torch.tensor([[1], [2], [3]], dtype=torch.float)
print('A:\n', A)
print('b:\n', b)
(LU_data, LU_pivots) = torch.lu(A)
print('LU_data:\n', LU_data)
print('LU_pivots:\n', LU_pivots)
x = torch.lu_solve(b, LU_data, LU_pivots)
print('x:\n', x)
print('A * x:\n', torch.mm(A, x))