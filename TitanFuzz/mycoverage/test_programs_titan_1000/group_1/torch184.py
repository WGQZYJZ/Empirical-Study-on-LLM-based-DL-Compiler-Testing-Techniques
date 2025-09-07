import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10, 10)
result = torch.lt(data, 0.5)