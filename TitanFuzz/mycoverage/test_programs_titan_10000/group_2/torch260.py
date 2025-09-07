import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 3)
torch.Tensor.int(input_tensor, memory_format=torch.preserve_format)