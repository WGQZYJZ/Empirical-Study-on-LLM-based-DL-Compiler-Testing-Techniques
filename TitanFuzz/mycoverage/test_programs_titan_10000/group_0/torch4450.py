import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 1, 2)
torch.Tensor.istft(input_tensor, 2)