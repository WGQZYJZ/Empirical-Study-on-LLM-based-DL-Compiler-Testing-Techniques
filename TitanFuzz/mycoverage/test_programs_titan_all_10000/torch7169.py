import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 2, 3, 4])
torch.combinations(input, r=2, with_replacement=False)