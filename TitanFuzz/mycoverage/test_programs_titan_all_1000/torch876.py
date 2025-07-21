import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
torch.nn.init.normal_(input_tensor, mean=0.0, std=1.0)