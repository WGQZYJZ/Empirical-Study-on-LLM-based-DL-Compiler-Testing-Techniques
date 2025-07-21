import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 17, dtype=torch.float32).reshape(1, 1, 4, 4)
output = torch.Tensor.q_per_channel_zero_points(input_tensor)