import torch
from torch import nn
from torch.autograd import Variable

data = torch.rand(3, 4)
result = torch.expm1(data)
result = torch.expm1_(data)