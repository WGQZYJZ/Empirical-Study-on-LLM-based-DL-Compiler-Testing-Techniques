import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
det = torch.linalg.det(A)
A = torch.rand(3, 3)
det = torch.linalg.det(A)