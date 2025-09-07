import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5])
output = torch.repeat_interleave(x, repeats=3, dim=0)
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.roll(x, shifts=1, dims=1)