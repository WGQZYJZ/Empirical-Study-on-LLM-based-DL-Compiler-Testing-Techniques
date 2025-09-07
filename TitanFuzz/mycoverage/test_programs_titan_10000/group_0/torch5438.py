import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(100, 100)
input_data = torch.rand(100, 100)
torch.Tensor.copy_(input_tensor, input_data, non_blocking=False)