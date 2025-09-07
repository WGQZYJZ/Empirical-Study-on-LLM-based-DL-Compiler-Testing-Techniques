import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10, dtype=torch.float64)
result = torch.special.polygamma(1, data)