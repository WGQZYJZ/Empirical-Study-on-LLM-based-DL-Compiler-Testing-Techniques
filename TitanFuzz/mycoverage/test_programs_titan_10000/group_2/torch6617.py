import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(3, 4)
B = torch.linalg.pinv(A)