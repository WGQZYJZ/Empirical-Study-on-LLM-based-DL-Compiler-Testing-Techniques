import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 3)
conj_tensor = torch.conj(input_tensor)