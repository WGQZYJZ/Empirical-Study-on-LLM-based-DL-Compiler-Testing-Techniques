import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3)
result = torch.ge(data, 0.5)