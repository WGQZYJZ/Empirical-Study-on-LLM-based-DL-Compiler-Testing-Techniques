import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn((2, 3, 4, 5, 6))
lazy_bn = torch.nn.LazyBatchNorm3d(3)
lazy_bn(x)