import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
(U, S, V) = torch.svd(input)