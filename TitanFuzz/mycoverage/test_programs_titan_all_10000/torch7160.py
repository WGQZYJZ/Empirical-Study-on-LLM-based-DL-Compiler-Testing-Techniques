import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand((1, 2, 3, 4))
torch.Tensor.logit_(input_tensor)