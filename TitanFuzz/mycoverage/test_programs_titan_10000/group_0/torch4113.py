import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(4, 4)
torch.Tensor.log_normal_(input_tensor, mean=1, std=2)