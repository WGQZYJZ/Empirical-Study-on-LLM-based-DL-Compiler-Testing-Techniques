import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(4, 4)
split_tensor = torch.split(tensor, 4)
split_tensor = torch.split(tensor, 2, dim=1)
split_tensor = torch.split(tensor, [2, 2], dim=1)
split_tensor = torch.split(tensor, [2, 2], dim=0)