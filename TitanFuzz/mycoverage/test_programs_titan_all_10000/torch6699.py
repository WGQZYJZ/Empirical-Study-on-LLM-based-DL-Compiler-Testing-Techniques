import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
input = torch.tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
output = torch.nn.ZeroPad2d((2, 3, 1, 1))(input)