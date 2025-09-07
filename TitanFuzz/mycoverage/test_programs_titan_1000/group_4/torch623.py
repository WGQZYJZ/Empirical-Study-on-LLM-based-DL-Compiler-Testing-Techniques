import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3)
torch.Tensor.mul(input_tensor, 2)
input_tensor = torch.rand(1, 2, 3)
torch.Tensor.mul_(input_tensor, 2)