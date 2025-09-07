import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(5)
other = torch.rand(5)
maximum_result = torch.Tensor.maximum(input_tensor, other)