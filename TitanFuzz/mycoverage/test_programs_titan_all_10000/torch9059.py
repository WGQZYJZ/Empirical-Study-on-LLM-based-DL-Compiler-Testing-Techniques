import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
divisor = torch.tensor(2)
torch.Tensor.fmod_(input_tensor, divisor)