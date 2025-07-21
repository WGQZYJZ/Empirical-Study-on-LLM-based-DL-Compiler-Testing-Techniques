import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 3)
output_tensor = torch.Tensor.rad2deg(input_tensor)