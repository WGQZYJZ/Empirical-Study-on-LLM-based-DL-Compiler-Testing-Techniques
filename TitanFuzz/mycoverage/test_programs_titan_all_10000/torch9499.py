import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
pinv_A = torch.linalg.pinv(A)