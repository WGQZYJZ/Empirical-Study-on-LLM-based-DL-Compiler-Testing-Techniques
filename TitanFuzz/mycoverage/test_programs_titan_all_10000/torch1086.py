import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(10, requires_grad=True)
torch.distributed.is_nccl_available()
torch.distributed.is_available()
torch.distributed.is_mpi_available()
torch.distributed.is_gloo_available()