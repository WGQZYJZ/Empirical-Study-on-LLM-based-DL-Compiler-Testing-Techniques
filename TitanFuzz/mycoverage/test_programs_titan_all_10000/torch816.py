import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 3)
other = torch.rand(3)
result = torch.Tensor.inner(input_tensor, other)