import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 3)
(Q, R) = torch.linalg.qr(A)