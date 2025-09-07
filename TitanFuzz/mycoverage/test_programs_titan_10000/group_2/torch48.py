import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 1, 2, 2)
torch.Tensor.is_quantized(input_tensor)