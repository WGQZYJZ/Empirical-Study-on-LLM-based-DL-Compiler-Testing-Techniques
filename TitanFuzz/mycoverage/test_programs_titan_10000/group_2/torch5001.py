import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.q_per_channel_scales(_input_tensor)