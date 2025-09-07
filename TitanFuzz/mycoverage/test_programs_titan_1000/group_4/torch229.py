import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(100, 100)
corrcoef = torch.Tensor.corrcoef(input_tensor)