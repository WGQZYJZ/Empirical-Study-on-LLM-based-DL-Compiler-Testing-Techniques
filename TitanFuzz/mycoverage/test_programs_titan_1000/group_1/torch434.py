import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
corrcoef = torch.Tensor.corrcoef(input_tensor)