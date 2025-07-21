import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
flip_lr = torch.fliplr(input)