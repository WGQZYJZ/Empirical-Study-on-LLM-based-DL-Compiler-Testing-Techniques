import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
is_shared = torch.Tensor.is_shared(input_tensor)