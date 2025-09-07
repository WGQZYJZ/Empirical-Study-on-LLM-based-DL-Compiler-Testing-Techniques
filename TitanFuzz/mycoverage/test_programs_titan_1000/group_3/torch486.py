import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
indices = torch.tensor([[0, 0, 0], [2, 2, 2]], dtype=torch.int64)
output_tensor = torch.Tensor.take_along_dim(input_tensor, indices, dim=1)