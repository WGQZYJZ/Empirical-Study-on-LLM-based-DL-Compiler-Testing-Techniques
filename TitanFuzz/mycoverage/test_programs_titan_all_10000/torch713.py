import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.ByteTensor([[1, 0, 1], [1, 0, 0]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)