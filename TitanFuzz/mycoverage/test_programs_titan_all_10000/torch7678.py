import torch
from torch import nn
from torch.autograd import Variable
A = torch.Tensor([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
L = torch.linalg.cholesky(A)