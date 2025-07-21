import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([0, 1, 0, 1, 1])
bernoulli_tensor = torch.Tensor.bernoulli(input_tensor)