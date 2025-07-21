import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5, 5)
identity_layer = torch.nn.Identity()