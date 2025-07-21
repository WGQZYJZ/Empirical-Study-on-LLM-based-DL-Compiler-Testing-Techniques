import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(2, 2)
torch.nn.init.sparse_(tensor, sparsity=0.5)
tensor = torch.empty(2, 2)
torch.nn.init.xavier_normal_(tensor)