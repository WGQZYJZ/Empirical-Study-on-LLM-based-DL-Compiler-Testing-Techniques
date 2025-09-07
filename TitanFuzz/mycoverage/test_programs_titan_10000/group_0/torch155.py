import torch
from torch import nn
from torch.autograd import Variable

data = torch.rand(10, 3)
data_new = torch.vstack((data, data))