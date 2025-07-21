import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0.5, 1.0, 2.0, 3.0, 4.0, 5.0], dtype=torch.float32)
other = torch.tensor([0.5, 1.0, 2.0, 3.0, 4.0, 5.0], dtype=torch.float32)
output = torch.igammac(input, other)