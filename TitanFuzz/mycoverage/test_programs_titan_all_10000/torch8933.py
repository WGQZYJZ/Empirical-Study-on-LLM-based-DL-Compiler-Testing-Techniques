import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(2, 3)
torch.nn.init.sparse_(tensor, sparsity=0.2, std=0.01)