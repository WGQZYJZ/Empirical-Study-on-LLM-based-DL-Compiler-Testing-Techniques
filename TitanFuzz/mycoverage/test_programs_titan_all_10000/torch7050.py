import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4, 5)
output = torch.Tensor.logit_(input_tensor)