import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.rand(5, 3))
y = torch.special.exp2(x)