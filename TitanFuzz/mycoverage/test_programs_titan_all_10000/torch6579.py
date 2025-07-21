import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
log1p_out = torch.Tensor.log1p_(input_tensor)