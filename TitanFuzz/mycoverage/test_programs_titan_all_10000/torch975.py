import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other_tensor = torch.rand(3, 3)
max_tensor = torch.maximum(input_tensor, other_tensor)