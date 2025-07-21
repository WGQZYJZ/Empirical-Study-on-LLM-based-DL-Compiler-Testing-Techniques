import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, dtype=torch.float32)
torch.Tensor.cos_(input_tensor)