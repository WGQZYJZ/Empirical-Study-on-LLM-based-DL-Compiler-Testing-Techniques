import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1)
radian = (math.pi * input_data)
degree = torch.rad2deg(radian)