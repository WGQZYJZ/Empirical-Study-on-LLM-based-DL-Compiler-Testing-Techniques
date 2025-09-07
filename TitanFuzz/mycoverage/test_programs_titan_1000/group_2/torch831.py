import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
(q, r) = torch.qr(input)