import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
B = torch.randn(3, 2)
X = torch.linalg.solve(A, B)