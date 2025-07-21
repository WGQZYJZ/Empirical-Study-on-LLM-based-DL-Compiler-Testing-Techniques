import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
(sign, logdet) = torch.linalg.slogdet(A)