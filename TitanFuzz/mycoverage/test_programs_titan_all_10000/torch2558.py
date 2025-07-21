import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3, 4, 5)
torch.Tensor.sum_to_size(input_tensor, 1, 2, 3, 4, 5)