import torch
from torch import nn
from torch.autograd import Variable
input_1 = torch.rand(2, 3, 4)
input_2 = torch.rand(2, 3, 4)
output = torch.dstack((input_1, input_2))