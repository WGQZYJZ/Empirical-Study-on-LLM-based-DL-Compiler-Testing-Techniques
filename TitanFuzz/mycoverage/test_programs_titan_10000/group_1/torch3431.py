import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([0, (math.pi / 4), (math.pi / 2), ((3 * math.pi) / 4), math.pi])
y = torch.arctan(x)