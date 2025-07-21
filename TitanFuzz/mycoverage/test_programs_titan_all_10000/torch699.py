import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([3.0, 2.0, 1.0])
torch.nextafter(input, other)
torch.nextafter(input, other, out=input)