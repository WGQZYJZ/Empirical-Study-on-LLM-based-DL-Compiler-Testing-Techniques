'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_nccl_available\ntorch.distributed.is_nccl_available()\n'
import torch
x = torch.randn(3, 2)
y = torch.randn(3, 2)
torch.distributed.is_nccl_available()
torch.distributed.is_mpi_available()