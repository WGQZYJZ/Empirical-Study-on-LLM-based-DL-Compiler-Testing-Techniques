import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
result_tensor = torch.Tensor.index_add_(input_tensor, 0, torch.tensor([0, 1]), torch.tensor([[1, 1, 1], [1, 1, 1]]))