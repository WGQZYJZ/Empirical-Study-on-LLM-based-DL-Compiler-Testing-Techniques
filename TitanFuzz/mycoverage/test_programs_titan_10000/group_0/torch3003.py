import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(5, 3)
torch.Tensor.resolve_conj(input_tensor)