import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
torch.set_default_dtype(torch.float64)