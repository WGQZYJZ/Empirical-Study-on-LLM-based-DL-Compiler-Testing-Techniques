import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
move_axis_tensor = torch.Tensor.moveaxis(input_tensor, 0, (- 1))