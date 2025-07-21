import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
ceil_data = torch.ceil(input_data)