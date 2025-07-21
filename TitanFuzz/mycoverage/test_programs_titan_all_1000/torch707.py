import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3, 3)
threshold = 0.5
value = (- 1)
y = torch.nn.Threshold(threshold, value)(x)