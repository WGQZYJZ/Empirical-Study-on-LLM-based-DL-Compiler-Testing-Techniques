import torch
from torch import nn
from torch.autograd import Variable
data_1 = torch.rand(4, 4)
data_2 = torch.rand(4, 4)
data_3 = torch.column_stack((data_1, data_2))