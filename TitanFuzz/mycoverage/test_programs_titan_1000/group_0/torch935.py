import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(4, 4)
A = torch.mm(A.t(), A)
L = torch.linalg.cholesky(A)