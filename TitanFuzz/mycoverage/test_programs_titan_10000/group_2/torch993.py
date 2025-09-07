import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.arange(start=0, end=5, step=1)
torch.Tensor.lt_(input_tensor, other=3)