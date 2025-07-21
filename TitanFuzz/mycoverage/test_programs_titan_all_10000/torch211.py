import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 224, 224)
torch.nn.init.xavier_normal_(input_tensor, gain=1.0)