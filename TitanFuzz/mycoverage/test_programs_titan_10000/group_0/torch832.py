import torch
from torch import nn
from torch.autograd import Variable

data1 = torch.randn(3, 4)
data2 = torch.randn(3, 4)
result = torch.greater(data1, data2)