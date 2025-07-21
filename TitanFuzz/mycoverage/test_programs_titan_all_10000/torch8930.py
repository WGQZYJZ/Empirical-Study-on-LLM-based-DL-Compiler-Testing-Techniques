import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
torch.Tensor.sum_to_size(input_tensor, 2, 3)