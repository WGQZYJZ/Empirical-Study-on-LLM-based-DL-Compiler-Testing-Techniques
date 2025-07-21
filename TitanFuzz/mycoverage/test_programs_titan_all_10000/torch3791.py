import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(5, 3, 10))
h0 = Variable(torch.randn(2, 3, 20))
c0 = Variable(torch.randn(2, 3, 20))
lstm = torch.nn.LSTM(10, 20, 2)
(output, hn) = lstm(input, (h0, c0))