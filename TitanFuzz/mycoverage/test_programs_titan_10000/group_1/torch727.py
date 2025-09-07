import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.ones((2, 2))
result = torch.Tensor.multiply(input_tensor, 10)