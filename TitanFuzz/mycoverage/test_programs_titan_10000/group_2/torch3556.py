import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn((2, 3))
A_inv = torch.linalg.pinv(A)