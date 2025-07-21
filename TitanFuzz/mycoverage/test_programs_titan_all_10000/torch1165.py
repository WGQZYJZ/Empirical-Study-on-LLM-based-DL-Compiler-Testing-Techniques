import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3, 4, 5)
torch.Tensor.q_per_channel_scales(input_tensor)