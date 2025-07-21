import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
out = torch.Tensor.sub(input_tensor, other)