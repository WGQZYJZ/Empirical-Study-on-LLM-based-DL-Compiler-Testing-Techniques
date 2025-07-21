import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3)
torch.nn.init.uniform_(input_tensor, a=0.0, b=1.0)