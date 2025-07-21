import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)