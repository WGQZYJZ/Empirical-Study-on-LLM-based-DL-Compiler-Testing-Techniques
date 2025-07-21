'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triangular_solve\ntorch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
from torch.autograd import Variable
A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)
print('A:')
print(A)
print('b:')
print(b)
print('x:')
print(x)