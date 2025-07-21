import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
end = torch.ones(3, 3)
weight = 0.5
torch.Tensor.lerp_(input_tensor, end, weight)