import torch
from torch import nn
from torch.autograd import Variable

data = torch.arange(0, 9)
split = torch.tensor_split(data, 3, dim=0)