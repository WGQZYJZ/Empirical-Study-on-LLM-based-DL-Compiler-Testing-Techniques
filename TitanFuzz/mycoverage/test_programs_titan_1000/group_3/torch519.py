import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0, 30, 45, 60, 90])
output = torch.deg2rad(input)