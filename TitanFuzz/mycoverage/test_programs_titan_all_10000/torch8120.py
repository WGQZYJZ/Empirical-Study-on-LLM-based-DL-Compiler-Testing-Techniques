import torch
from torch import nn
from torch.autograd import Variable
data = torch.ones(2, 3)
data_ravel = torch.ravel(data)