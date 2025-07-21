import torch
from torch import nn
from torch.autograd import Variable
weights = torch.tensor([0.2, 0.8])
out = torch.multinomial(weights, 1)