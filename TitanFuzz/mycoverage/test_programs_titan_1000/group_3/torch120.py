import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(3, 4)
torch.Tensor.fill_(input_tensor, 1.0)