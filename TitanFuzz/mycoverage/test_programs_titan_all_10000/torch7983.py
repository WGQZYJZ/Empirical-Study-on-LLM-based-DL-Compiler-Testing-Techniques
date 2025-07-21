import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
flipped_input = torch.flip(input, [0])