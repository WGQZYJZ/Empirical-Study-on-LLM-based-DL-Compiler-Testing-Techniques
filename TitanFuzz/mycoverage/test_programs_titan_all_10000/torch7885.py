import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
value = 2
torch.Tensor.mul_(input_tensor, value)