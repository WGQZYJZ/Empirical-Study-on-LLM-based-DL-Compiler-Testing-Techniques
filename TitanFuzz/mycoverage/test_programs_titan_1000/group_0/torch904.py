import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
torch.set_default_dtype(torch.float32)