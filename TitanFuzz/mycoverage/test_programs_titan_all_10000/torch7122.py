import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 1, dtype=torch.float)
torch.Tensor.polygamma_(input_tensor, 1)