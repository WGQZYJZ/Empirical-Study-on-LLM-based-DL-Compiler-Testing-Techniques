import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 4, 5, 6)
_output_tensor = torch.Tensor.q_per_channel_axis(_input_tensor)