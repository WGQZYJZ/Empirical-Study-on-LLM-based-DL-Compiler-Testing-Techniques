import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
b = torch.cholesky(a, upper=False)
c = torch.mm(b, torch.t(b))