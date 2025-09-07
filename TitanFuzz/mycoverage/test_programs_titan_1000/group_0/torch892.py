import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(2, 3)
torch.nn.init.sparse_(tensor, sparsity=0.5)