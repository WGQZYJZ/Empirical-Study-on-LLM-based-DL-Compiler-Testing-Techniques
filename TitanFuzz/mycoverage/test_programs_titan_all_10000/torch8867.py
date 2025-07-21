import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
det_A = torch.linalg.det(A)