import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3)
indices = torch.tensor([[0, 1, 2], [1, 1, 1]])
values = torch.tensor([1, 2])
output_tensor = torch.Tensor.index_put(input_tensor, indices, values, accumulate=False)