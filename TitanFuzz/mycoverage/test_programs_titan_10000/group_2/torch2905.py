import torch
from torch import nn
from torch.autograd import Variable

torch.distributed.is_mpi_available()
torch.distributed.is_nccl_available()