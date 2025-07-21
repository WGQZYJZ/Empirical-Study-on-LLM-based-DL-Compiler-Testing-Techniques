import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4, 5)
torch.Tensor.resolve_conj(input_tensor)