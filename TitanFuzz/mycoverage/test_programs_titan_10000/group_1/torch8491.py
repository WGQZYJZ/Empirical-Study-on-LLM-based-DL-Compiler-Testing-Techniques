import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(1, 3, 5, 5))
y = torch.nn.functional.hardtanh(x)