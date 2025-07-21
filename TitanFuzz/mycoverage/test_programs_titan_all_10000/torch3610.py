import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4, 4)
indices = torch.tensor([[1, 2, 3], [0, 1, 2], [0, 1, 2], [1, 2, 3]])
values = torch.tensor([1, 2, 3, 4])
output_tensor = torch.Tensor.index_put(input_tensor, indices, values, accumulate=False)