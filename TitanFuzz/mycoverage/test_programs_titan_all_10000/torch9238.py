import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[6.8, (- 2.11), 5.66, 5.97, 8.23], [(- 6.05), (- 3.3), 5.36, (- 4.44), 1.08], [(- 0.45), 2.58, (- 2.7), 0.27, 9.04], [8.32, 2.71, 4.35, (- 7.17), 2.14], [(- 9.67), (- 5.14), (- 7.26), 6.08, (- 6.87)]])
b = torch.tensor([[4.02], [6.19], [(- 8.22)], [(- 7.57)], [(- 3.03)]])
(LU_data, LU_pivots) = torch.lu(A)
x = torch.lu_solve(b, LU_data, LU_pivots)