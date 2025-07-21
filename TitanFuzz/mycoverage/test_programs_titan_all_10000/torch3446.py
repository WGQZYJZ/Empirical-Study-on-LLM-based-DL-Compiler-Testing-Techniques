import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(5, 5)
y = torch.clone(x)
y.fill_(2)