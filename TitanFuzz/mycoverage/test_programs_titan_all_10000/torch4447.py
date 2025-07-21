import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(2, 2))
selu = torch.nn.SELU(inplace=False)
y = selu(x)