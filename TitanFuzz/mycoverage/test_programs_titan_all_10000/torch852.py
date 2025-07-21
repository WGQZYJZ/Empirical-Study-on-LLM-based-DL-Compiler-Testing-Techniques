import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A_inv = torch.linalg.inv(A)
I = torch.matmul(A, A_inv)