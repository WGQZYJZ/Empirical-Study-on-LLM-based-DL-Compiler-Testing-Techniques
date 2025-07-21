import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([2, 3, 4])
torch.Tensor.rsqrt_(input_tensor)