import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
flipped_tensor = torch.Tensor.flipud(input_tensor)