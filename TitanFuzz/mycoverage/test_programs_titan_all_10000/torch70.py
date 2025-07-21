import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
torch.Tensor.resize_as_(input_tensor, torch.rand(2, 3, 4))