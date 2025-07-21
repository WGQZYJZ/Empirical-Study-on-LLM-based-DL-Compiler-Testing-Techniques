import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(3, 4))
torch.nn.functional.pdist(x, p=2)
x = Variable(torch.randn(3, 4))
torch.nn.functional.pdist(x, p=2)