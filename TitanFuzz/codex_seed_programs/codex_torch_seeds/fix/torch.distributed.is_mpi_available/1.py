'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_mpi_available\ntorch.distributed.is_mpi_available()\n'
import torch
import torch.distributed as dist
print(dist.is_mpi_available())
print(dist.is_nccl_available())
print(dist.is_gloo_available())