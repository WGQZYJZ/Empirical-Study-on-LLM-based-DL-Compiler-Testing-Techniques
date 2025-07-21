import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3, requires_grad=True)
torch.distributed.is_nccl_available()