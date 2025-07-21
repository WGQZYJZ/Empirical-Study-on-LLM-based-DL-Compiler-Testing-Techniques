import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5, 7)
gru = torch.nn.GRU(7, 3)
(out, hidden) = gru(x)