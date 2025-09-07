import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3, 4)
shifts = torch.tensor([1, 2])
result = torch.Tensor.roll(input_tensor, shifts, dims=0)