import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(2, 3))
softmax = torch.nn.Softmax(dim=1)
result = softmax(x)