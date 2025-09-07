import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0, (- 1.0), 1.0, (- 1.0)], dtype=torch.float32)
other = torch.tensor([1.0, 1.0, (- 1.0), (- 1.0)], dtype=torch.float32)
output = torch.atan2(input, other)