import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float64)
other = torch.tensor([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype=torch.float64)
result = torch.Tensor.igammac_(input_tensor, other)