import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0.0, 30.0, 45.0, 60.0, 90.0])
output = torch.deg2rad(input)