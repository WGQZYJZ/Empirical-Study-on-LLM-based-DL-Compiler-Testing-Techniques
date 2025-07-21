import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
torch.Tensor.sinc_(input_tensor)