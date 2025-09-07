import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(10, 3)
torch.distributed.is_available()
input_data = torch.randn(10, 3)
torch.distributed.is_initialized()