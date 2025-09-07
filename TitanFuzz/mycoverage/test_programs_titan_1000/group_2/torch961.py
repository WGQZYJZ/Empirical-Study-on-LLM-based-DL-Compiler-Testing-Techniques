import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4, 5).float()
torch.Tensor.q_per_channel_axis(input_tensor)