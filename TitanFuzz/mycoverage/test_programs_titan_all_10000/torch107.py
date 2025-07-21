import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1000, 1000)
torch.distributed.is_nccl_available()