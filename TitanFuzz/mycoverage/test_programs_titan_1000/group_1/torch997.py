import torch
from torch import nn
from torch.autograd import Variable
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
A = torch.from_numpy(A)
b = torch.from_numpy(b)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)