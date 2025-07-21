import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4, 4)
torch.Tensor.q_per_channel_axis(input_tensor)