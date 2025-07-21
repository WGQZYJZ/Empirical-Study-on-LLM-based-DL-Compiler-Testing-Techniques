import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, dtype=torch.float)
torch.special.psi(input_data)