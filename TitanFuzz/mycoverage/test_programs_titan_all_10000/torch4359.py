import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3)
end = torch.rand(3)
weight = torch.rand(1)
output = torch.lerp(input, end, weight)