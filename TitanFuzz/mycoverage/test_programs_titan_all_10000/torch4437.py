import torch
from torch import nn
from torch.autograd import Variable
abs_data = torch.rand(3, 3)
angle_data = torch.rand(3, 3)
out_data = torch.polar(abs_data, angle_data)