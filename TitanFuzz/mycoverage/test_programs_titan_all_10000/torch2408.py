import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
result_tensor = torch.Tensor.log1p_(input_tensor)