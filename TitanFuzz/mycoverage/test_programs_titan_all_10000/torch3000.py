import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4, 5, 6, dtype=torch.float32)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)