import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(3, 3)
sum_tensor = torch.Tensor.sum_to_size(input_tensor, (1, 1))