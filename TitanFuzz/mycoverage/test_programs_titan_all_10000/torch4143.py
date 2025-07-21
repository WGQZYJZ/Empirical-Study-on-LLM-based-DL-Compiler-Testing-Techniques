import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 5, 3, 3)
softmax2d = torch.nn.Softmax2d()
output = softmax2d(input)