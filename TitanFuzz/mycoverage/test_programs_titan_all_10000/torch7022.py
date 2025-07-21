import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
end = torch.randn(10, 10)
weight = torch.randn(10, 10)
out = torch.Tensor.lerp_(input_tensor, end, weight)