import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([0, 30, 45, 60, 90])
radians = torch.Tensor.deg2rad(input_data)