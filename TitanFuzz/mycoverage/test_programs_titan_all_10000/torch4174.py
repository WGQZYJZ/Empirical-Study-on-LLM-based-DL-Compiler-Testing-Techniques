import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
softmax = torch.nn.Softmin(dim=0)
output = softmax(x)
softmax = torch.nn.Softmin(dim=1)
output = softmax(x)