import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100, 100)
other_data = torch.randn(100, 100)
torch.special.xlog1py(input_data, other_data)