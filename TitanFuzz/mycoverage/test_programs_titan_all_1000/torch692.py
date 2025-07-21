import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
b = torch.tensor([[1], [2], [3]], dtype=torch.float)
(LU_data, LU_pivots) = torch.lu(A)
x = torch.lu_solve(b, LU_data, LU_pivots)