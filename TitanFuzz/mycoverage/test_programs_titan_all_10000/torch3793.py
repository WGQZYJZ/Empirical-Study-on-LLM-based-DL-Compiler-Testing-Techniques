import torch
from torch import nn
from torch.autograd import Variable
input_tensor = ((torch.rand(4, 4) * 20) - 10)
acos_tensor = torch.acos(input_tensor)