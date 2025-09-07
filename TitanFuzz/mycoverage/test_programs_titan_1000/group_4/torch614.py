import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 4)
(q, r) = torch.linalg.qr(A)