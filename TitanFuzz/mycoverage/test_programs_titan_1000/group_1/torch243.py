import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(size=(3, 3))
detached_tensor = torch.Tensor.detach(input_tensor)