import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
angle_tensor = torch.Tensor.angle(input_tensor)