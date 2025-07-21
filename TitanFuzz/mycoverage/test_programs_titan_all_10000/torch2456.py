import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]]))
pool = torch.nn.AdaptiveMaxPool1d(3)
output = pool(input)