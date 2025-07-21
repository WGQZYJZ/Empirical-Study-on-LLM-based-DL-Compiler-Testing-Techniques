import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5, 6)
torch.Tensor.q_per_channel_scales(_input_tensor)