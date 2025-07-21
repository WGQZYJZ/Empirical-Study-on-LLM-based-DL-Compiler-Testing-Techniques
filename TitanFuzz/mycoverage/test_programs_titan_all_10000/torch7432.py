import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.uint8)
other = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.uint8)
torch.Tensor.logical_and_(input_tensor, other)