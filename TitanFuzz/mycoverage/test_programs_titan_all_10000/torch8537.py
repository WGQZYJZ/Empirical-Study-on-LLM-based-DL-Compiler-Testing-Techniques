import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.tril(input, diagonal=0)
output = torch.tril(input, diagonal=1)
output = torch.tril(input, diagonal=(- 1))
output = torch.tril(input, diagonal=2)
output = torch.tril(input, diagonal=(- 2))