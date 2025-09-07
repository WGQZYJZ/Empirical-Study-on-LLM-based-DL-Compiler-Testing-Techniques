import torch
from torch import nn
from torch.autograd import Variable

data = torch.randn(3, 4)
(value, index) = torch.kthvalue(data, 2, 1)