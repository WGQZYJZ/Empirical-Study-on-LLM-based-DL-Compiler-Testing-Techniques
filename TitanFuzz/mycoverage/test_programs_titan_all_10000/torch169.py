import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
output_tensor = torch.Tensor.less_equal_(input_tensor, other)