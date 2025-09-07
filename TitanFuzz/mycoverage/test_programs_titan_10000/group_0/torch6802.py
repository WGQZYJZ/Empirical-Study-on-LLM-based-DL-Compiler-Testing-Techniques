import torch
from torch import nn
from torch.autograd import Variable

input = torch.randint(1, 10, (5,))
output = torch.combinations(input, r=2, with_replacement=False)