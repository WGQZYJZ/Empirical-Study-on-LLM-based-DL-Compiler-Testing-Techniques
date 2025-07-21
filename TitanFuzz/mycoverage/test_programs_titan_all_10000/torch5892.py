import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 1, 5, 5)
torch.Tensor.sinc_(input_tensor)