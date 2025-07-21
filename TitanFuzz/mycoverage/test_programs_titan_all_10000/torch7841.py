import torch
from torch import nn
from torch.autograd import Variable
output = torch.ormqr(input, tau, other, left=True, transpose=False)