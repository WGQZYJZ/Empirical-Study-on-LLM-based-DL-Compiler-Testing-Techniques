import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.index_put_(input_tensor, indices, values, accumulate=False)