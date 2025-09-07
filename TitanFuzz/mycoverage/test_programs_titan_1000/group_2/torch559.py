import torch
from torch import nn
from torch.autograd import Variable
tensors = (torch.rand(2, 3), torch.rand(2, 3))
out = torch.row_stack(tensors)