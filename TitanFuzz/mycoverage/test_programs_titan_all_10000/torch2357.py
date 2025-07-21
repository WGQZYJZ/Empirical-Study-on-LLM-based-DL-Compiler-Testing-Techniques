import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
(Q, R) = torch.linalg.qr(A)
A = torch.randn(3, 3)
(U, S, V) = torch.linalg.svd(A)