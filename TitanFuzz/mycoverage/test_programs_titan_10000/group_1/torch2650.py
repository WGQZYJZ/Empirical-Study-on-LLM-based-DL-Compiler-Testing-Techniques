import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(4, 4)
(Q, R) = torch.linalg.qr(A)