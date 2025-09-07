import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
flatten_layer = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
flatten_tensor = flatten_layer(input_tensor)