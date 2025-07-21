import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
indices = torch.Tensor.indices(input_tensor)