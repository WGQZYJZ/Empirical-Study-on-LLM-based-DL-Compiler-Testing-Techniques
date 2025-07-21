import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
is_meta = torch.Tensor.is_meta(input_tensor)