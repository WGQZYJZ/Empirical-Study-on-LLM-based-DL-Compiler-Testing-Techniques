import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(3, 3)
eigvalsh = torch.linalg.eigvalsh(A)