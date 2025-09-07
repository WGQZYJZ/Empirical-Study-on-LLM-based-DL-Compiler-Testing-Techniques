import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(5, 5), requires_grad=True)
torch.nn.init.xavier_uniform_(x)