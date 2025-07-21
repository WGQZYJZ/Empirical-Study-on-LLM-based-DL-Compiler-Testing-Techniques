import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 3, 3)
threshold = torch.nn.Threshold(0.5, 0)
out = threshold(x)