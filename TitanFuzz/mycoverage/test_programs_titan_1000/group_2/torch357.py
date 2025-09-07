import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 16, 1)
input_tensor = input_tensor.view(4, 4)
split_tensor = torch.Tensor.vsplit(input_tensor, 2)