import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 3, 3)
output = torch.Tensor.deg2rad(input_data)