import torch
from torch import nn
from torch.autograd import Variable

A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float64)
inv_A = torch.linalg.inv_ex(A)