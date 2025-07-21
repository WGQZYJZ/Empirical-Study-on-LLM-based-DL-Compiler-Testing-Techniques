import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
torch.Tensor.sub_(input_tensor, other_tensor)