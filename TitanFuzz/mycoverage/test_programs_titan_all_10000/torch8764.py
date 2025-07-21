import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 3)
cov_result = torch.Tensor.cov(input_tensor)