import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1e-323], dtype=torch.float64)
torch.set_flush_denormal(True)