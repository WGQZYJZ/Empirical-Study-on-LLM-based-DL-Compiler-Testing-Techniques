import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)