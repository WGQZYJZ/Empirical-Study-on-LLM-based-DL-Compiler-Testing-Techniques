import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [3.0, 6.0, 9.0]])
B = torch.linalg.cholesky_ex(A)