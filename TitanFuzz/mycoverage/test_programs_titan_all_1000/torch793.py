import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
softmax = torch.nn.Softmin(dim=1)
output = softmax(input)