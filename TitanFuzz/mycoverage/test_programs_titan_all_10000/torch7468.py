import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
gt_result = torch.Tensor.gt_(input_tensor, other)