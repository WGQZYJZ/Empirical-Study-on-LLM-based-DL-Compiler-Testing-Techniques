'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_mpi_available\ntorch.distributed.is_mpi_available()\n'
import torch
from torch.distributed import is_mpi_available
if True:
    print('is_mpi_available:', is_mpi_available())