import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
xlogy_ = torch.Tensor.xlogy_(input_tensor, other)