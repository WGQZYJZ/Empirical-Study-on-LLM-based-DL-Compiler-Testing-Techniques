import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
bfloat16_tensor = torch.Tensor.bfloat16(input_tensor)