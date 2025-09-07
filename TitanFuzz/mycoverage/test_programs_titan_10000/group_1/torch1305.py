import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(3, 3)
B = torch.rand(3, 3)
X = torch.linalg.solve(A, B)