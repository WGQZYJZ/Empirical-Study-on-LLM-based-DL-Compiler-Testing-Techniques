import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 5)
other = torch.rand(3, 5)
result = torch.Tensor.minimum(input_tensor, other)