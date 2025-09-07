import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randint(low=0, high=10, size=(1, 5))
torch.Tensor.round_(input_tensor)