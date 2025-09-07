import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4, 5)
torch.Tensor.q_per_channel_axis(_input_tensor)