import torch
from torch import nn
from torch.autograd import Variable

data_tensor = torch.randn(4, 4)
result = torch.Tensor.nextafter_(data_tensor, 1)