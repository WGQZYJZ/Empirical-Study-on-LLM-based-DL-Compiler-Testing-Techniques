import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 3, dtype=torch.float)
end = torch.rand(4, 3, dtype=torch.float)
weight = torch.rand(4, 3, dtype=torch.float)
out = torch.lerp(input, end, weight)