import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
(Q, R) = torch.qr(input)
input = torch.randn(3, 3)
(Q, R) = torch.qr(input)