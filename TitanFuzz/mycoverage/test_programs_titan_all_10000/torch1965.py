import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.randn(4, 4)
torch.Tensor.lerp_(input_tensor, end, weight)