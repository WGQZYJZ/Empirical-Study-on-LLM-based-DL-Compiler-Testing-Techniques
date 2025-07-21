import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(3, 2), dtype=torch.int32)
torch.Tensor.transpose_(input_tensor, 0, 1)