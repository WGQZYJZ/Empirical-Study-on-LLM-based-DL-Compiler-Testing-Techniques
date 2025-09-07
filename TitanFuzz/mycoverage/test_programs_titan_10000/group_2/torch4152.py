import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 3, 1, 1)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (2, 3, 4, 5))