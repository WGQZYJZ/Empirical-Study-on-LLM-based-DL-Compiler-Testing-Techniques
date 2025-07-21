import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 20)
device_tensor = torch.Tensor.device(input_tensor)