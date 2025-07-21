import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
B = torch.tensor([[1.0, 2.0], [1.0, 2.0]])
X = torch.linalg.lstsq(A, B)