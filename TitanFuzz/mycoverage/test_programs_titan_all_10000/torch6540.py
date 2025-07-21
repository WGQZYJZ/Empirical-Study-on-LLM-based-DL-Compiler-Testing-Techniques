import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
lt_result = torch.Tensor.lt_(input_tensor, 0)