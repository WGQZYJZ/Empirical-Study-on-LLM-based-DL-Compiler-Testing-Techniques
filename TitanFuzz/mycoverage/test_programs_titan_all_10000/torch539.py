import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
end = torch.randn(3, 4)
weight = torch.randn(1)
output = torch.lerp(input, end, weight)