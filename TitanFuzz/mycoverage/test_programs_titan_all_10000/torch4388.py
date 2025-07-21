import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randint(5, (3, 3), dtype=torch.int)
torch.Tensor.ldexp_(input_tensor, other)