import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(5, 3)
relu6 = torch.nn.ReLU6()