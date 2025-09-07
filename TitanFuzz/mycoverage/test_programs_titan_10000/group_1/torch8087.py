import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
less_equal = torch.Tensor.less_equal_(input_tensor, other)