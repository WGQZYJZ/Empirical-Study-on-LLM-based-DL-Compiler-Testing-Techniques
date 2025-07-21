import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
device = torch.Tensor.device(input_tensor)