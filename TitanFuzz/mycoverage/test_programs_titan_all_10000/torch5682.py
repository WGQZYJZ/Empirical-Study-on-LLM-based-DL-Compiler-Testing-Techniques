import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
torch.nn.init.dirac_(input_data, groups=1)