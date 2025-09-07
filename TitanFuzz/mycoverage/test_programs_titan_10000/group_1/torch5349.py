import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(2, 3))
y = torch.nn.functional.elu(x, alpha=1.0, inplace=False)