import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4, 5)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)