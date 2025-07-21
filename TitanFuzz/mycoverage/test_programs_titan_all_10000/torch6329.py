import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2)
torch.package.Directory(input_data, True)