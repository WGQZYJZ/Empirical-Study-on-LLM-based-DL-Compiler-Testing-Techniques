import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
result = torch.nn.Tanhshrink()(a)