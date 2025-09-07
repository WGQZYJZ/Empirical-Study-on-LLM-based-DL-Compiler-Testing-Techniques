import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10, 10, 10)
other = torch.rand(10, 10, 10, 10)
torch.Tensor.dist(input_tensor, other, p=2)