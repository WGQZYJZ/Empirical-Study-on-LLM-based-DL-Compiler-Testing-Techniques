import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A_sym = ((A + A.t()) / 2)
eigen_values = torch.linalg.eigvalsh(A_sym)