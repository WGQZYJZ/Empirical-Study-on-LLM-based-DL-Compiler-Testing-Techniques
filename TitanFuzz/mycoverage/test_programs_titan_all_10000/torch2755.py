import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
end = torch.randn(3, 3)
weight = torch.randn(3, 3)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)