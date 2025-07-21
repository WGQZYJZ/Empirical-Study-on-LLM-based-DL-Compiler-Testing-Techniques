'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_nccl_available\ntorch.distributed.is_nccl_available()\n'
import torch
import os
import torch
import torch.distributed as dist
data = torch.randn(10, requires_grad=True)
torch.distributed.is_nccl_available()
torch.distributed.is_available()
torch.distributed.is_mpi_available()
torch.distributed.is_gloo_available()