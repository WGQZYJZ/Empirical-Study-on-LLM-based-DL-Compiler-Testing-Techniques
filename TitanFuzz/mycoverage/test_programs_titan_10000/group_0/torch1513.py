import torch
from torch import nn
from torch.autograd import Variable

A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
torch.linalg.det(A)