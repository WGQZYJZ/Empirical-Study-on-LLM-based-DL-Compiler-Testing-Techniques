import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
result = torch.Tensor.erfinv(input_tensor)