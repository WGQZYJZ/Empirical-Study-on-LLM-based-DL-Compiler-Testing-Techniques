import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
torch.Tensor.q_per_channel_zero_points(_input_tensor)