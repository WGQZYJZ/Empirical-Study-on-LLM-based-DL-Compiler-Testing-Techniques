import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3)
torch.Tensor.sigmoid_(input_tensor)