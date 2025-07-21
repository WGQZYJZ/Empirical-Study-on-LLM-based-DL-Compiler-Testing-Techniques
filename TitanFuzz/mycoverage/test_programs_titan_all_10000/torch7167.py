import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
indices = torch.tensor([0, 1, 2, 3, 4])
result = torch.Tensor.take(input_tensor, indices)