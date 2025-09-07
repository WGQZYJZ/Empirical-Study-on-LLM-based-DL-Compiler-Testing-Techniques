import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(2, 3))
prelu = torch.nn.PReLU()