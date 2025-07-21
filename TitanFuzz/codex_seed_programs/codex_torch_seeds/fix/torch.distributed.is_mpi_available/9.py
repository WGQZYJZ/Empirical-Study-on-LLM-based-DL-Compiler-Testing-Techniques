'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_mpi_available\ntorch.distributed.is_mpi_available()\n'
import torch
print(torch.__version__)
data = torch.ones(10)
print(torch.distributed.is_mpi_available())