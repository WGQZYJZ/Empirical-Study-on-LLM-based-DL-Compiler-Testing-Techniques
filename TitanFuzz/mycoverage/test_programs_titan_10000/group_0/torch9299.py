import torch
from torch import nn
from torch.autograd import Variable

data = torch.randn(5, 5)
result = torch.frac(data)