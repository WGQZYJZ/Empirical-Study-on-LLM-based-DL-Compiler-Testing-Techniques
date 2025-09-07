import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([0, (math.pi / 2), math.pi, ((3 * math.pi) / 2), (2 * math.pi)])
output = torch.rad2deg(input)