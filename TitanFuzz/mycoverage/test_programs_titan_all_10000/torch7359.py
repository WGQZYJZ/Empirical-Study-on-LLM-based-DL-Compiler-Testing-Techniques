import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
polygamma = torch.special.polygamma(1, input)