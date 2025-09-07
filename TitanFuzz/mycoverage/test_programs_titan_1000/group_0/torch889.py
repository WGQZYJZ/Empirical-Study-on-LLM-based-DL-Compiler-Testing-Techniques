import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(4, 4)
B = torch.randn(4, 4)
C = torch.linalg.matmul(A, B)
D = torch.matmul(A, B)
E = torch.mm(A, B)