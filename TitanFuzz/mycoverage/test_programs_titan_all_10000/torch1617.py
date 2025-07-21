import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([0, (math.pi / 2), math.pi])
output_tensor = torch.Tensor.rad2deg(input_tensor)