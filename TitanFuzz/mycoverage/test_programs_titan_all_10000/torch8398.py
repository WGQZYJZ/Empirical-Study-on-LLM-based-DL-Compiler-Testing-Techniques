import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(2, 2)
det = torch.linalg.det(A)