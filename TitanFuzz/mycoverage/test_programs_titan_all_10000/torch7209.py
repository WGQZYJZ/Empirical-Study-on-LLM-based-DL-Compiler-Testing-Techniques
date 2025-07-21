import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 6).view(2, 3)
torch.Tensor.renorm_(input_tensor, p=1, dim=1, maxnorm=5)