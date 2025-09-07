import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(2, 2, 2)
output_tensor = torch.Tensor.q_per_channel_scales(input_tensor)