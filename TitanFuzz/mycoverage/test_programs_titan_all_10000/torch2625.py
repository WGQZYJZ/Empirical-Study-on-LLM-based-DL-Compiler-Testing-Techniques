import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
torch.Tensor.log10_(input_tensor)