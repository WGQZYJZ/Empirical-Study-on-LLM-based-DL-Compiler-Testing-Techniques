import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(10, 10))
dropout = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout(x)