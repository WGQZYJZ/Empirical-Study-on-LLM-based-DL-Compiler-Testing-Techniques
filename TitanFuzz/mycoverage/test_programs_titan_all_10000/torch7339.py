import torch
from torch import nn
from torch.autograd import Variable
A = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
L = torch.linalg.cholesky_ex(A, upper=False)