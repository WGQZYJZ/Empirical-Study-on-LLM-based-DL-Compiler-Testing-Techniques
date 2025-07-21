import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 3)
other = torch.rand(5, 3)
output_tensor = torch.Tensor.less_equal(input_tensor, other)