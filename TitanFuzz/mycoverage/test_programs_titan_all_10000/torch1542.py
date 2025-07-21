import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.tile(input_tensor, dims=(1, 2))