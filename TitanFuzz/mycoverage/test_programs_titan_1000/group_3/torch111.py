import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
det = torch.linalg.det(A)