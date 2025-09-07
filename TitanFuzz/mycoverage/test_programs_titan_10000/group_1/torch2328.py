import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
res = torch.Tensor.i0(input_tensor)