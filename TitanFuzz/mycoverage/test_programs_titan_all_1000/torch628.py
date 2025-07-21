import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
torch.optim.SparseAdam(input_data, lr=0.001, betas=(0.9, 0.999), eps=1e-08)