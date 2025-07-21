import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
torch.cross(input, other, dim=1)