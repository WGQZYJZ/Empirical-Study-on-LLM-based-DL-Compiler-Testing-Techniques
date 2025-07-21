import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
result = torch.Tensor.sub_(input_tensor, other)