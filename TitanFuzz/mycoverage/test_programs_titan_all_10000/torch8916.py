import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.randn(4, 4)
result = torch.less_equal(x, y)