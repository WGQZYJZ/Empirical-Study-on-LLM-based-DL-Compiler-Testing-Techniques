import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 5)
(q, r) = torch.linalg.qr(A)