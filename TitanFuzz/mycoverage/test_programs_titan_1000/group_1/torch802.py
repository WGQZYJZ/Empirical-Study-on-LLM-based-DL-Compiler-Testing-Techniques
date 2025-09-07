import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
torch.nn.init.uniform_(input_data, a=0.0, b=1.0)