import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
other = torch.rand(2, 3, 4)
torch.Tensor.reshape_as(input_tensor, other)