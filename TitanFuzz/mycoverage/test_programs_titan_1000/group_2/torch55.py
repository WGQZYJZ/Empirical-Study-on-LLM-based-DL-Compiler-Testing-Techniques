import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 11)
torch.Tensor.cauchy_(input_tensor)