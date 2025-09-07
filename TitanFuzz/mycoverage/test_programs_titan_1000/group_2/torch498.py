import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(5, 5)
B = torch.rand(5, 5)
inv_A = torch.linalg.inv(A)