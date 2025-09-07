import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
threshold = torch.nn.Threshold(0.5, 0.5)
y = threshold(x)