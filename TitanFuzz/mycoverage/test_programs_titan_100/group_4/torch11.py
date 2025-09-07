import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4, 4, 4)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)