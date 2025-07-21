import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(2, 3)
pinv_A = torch.linalg.pinv(A)
pinv_A = torch.linalg.pinv(A, rcond=1e-15)