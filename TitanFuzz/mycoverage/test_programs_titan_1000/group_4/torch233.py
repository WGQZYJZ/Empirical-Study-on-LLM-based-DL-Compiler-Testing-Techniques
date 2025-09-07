import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
corr_coeff = torch.Tensor.corrcoef(input_tensor)