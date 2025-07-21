import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 3, 4)
(U, S, V) = torch.linalg.svd(A)