import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 5, 5))
torch.nn.LPPool2d(norm_type=2, kernel_size=3, stride=2)
input = Variable(torch.randn(1, 3, 5, 5))