import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
pinv_data = torch.pinverse(input_data)