import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(4, 3, 2)
result = torch.numel(data)