import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3, 3)
other_tensor = torch.randn(3, 3, 3)
torch.Tensor.eq_(input_tensor, other_tensor)