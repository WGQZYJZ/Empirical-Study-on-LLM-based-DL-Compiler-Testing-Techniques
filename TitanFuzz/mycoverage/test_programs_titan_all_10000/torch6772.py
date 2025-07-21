import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
result = torch.Tensor.less_equal(input_tensor, 0)