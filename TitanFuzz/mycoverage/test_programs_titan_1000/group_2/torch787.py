import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
torch.Tensor.xlogy(input_tensor, other)
input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
torch.Tensor.xlogy(input_tensor, other)