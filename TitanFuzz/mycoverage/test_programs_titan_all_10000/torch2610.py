import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3)
trunc_tensor = torch.Tensor.trunc(input_tensor)
trunc_tensor = torch.trunc(input_tensor)