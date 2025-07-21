import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace((- 10), 10, steps=20)
y = torch.special.sinc(x)