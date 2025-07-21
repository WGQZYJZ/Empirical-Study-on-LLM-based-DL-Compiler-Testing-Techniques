import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
threshold = torch.nn.Threshold(0.5, 0.0)
output = threshold(input)