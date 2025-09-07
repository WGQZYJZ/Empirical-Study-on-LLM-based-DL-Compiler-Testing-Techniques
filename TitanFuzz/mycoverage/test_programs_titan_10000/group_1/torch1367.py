import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 2)
relu6 = torch.nn.ReLU6()