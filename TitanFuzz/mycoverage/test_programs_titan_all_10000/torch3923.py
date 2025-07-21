import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(- 180.0), (- 90.0), 0.0, 90.0, 180.0])
output = torch.deg2rad(input)