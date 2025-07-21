import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3, 4, 2)
result = torch.movedim(input_data, 0, (- 1))