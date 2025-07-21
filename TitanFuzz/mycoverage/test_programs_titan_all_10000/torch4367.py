import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 16).reshape(4, 4)
result = torch.vsplit(data, 4)
result = torch.vsplit(data, 2)
result = torch.hsplit(data, 4)
result = torch.hsplit(data, 2)
result = torch.split(data, 4, dim=0)
result = torch.split(data, 2, dim=0)