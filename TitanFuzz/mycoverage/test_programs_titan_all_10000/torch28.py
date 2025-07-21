import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
torch.linalg.eigvals(A)
A = torch.rand(3, 3)
torch.linalg.eig(A)