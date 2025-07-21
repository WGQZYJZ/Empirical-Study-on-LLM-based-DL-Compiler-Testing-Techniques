import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
torch.Tensor.transpose_(input_tensor, 0, 1)