import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
h = torch.randn(3, 5)
rnn = torch.nn.GRUCell(5, 5)
output = rnn(x, h)