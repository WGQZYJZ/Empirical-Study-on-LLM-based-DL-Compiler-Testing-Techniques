import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5, dtype=torch.float32)
torch.Tensor.q_per_channel_scales(input_tensor)