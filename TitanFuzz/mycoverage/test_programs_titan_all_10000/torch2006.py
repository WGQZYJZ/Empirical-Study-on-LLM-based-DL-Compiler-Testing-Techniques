import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([(- 1), 0, 1]))
y = torch.signbit(x)