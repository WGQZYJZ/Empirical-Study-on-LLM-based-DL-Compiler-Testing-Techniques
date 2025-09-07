import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 12, dtype=torch.float32)
output_tensor = torch.Tensor.random_(input_tensor)