import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 3, 3, 3)
atan_input_tensor = torch.Tensor.atan_(input_tensor)