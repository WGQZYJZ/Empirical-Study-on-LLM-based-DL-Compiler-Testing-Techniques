import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
power_A = torch.linalg.matrix_power(A, 2)