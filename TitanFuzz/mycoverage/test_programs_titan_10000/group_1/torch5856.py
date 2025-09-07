import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(3, 4, 5)
numel = torch.Tensor.numel(input_tensor)