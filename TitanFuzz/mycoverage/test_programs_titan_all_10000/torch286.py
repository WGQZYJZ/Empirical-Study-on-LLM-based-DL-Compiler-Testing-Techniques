import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 5)
softmax = torch.nn.Softmax(dim=1)
y = softmax(x)