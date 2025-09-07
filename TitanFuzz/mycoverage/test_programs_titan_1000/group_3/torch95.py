import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
device = torch.Tensor.get_device(input_data)