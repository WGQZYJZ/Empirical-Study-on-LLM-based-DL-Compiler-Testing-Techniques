import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
fixed_tensor = torch.Tensor.fix(input_tensor)