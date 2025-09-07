import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
cond_A = torch.linalg.cond(A)