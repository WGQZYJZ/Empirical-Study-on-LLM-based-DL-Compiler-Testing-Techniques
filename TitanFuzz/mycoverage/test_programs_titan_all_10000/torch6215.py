import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.tensor([[7, 8], [9, 10], [11, 12]])
index = torch.tensor([0, 2])
dim = 1
output_tensor = torch.Tensor.index_copy(input_tensor, dim, index, tensor2)