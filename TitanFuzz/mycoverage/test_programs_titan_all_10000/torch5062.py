import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], dtype=torch.float32)
output = torch.count_nonzero(input, dim=None)
output = torch.count_nonzero(input, dim=0)
output = torch.count_nonzero(input, dim=1)