import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
doubled_tensor = torch.Tensor.double(input_tensor, memory_format=torch.preserve_format)