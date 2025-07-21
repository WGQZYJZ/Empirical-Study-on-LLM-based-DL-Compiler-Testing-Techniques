import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(start=0, end=9, dtype=torch.float32).reshape(3, 3)
result = torch.Tensor.vsplit(data, 3)