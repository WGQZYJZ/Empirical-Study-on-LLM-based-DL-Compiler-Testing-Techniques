import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(10)
torch.distributed.is_nccl_available()