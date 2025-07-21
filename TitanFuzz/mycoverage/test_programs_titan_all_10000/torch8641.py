import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3, 4)
num_elements = torch.numel(x)