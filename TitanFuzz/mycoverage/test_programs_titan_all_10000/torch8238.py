import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(3, 3))
x_dropout = torch.nn.functional.alpha_dropout(x, p=0.5, training=False, inplace=False)