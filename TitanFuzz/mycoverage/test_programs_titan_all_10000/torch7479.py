import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]])
tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)