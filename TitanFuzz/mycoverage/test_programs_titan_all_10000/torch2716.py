import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
b = torch.tensor([[1.0], [2.0], [3.0]])
(x, _) = torch.lstsq(b, A)