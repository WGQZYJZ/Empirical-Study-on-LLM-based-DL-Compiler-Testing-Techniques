import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
torch.Tensor.lcm_(input_tensor, other)