import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3)
result = torch.Tensor.less_equal(input_tensor, 0)