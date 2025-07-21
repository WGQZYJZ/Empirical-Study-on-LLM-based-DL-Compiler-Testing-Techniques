import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 4)
pinv_A = torch.linalg.pinv(A)