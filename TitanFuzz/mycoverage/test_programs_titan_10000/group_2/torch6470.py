import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3, 4, 4)
output = torch.nn.Softmax2d()(input)