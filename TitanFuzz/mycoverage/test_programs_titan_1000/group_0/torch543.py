import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 3)
torch.Tensor.acos_(input_tensor)
input_tensor = torch.rand(1, 3, 3)
torch.acos(input_tensor)