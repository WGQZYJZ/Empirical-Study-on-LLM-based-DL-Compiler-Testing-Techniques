import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(4, 4)
torch.symeig(input, eigenvectors=False, upper=True)