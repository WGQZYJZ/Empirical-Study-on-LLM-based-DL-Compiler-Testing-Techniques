import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), requires_grad=True)
glu = torch.nn.GLU()
y = glu(x)
input = Variable(torch.randn(5, 3, 10))
h0 = Variable(torch.randn(2, 3, 20))
gru = torch.nn.GRU(10, 20, 2)
(out, hn) = gru(input, h0)