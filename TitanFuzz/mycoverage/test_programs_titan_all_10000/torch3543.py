import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4, 5)
logit_tensor = torch.Tensor.logit(input_tensor)