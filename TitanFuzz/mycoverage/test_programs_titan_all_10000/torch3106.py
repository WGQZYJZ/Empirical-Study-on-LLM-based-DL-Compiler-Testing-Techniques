import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])
torch.unique_consecutive(input)