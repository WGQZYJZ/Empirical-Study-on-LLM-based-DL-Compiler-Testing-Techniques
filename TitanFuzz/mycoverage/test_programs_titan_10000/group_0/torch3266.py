import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(1, 1, 5, 5))
torch.nn.Unfold(kernel_size=3, dilation=1, padding=0, stride=1)