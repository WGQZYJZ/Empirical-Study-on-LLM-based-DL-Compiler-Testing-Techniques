import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(5, 3)
result = torch.positive(data)