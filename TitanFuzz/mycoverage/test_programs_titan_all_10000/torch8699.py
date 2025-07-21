import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 32, 32)
output = torch.Tensor.q_scale(input_data)