import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(2, 3)
resolved_tensor = torch.Tensor.resolve_neg(input_tensor)