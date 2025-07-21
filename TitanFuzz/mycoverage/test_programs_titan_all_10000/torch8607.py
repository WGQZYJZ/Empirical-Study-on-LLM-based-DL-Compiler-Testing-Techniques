import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 2)
output = torch.view_as_complex(input)