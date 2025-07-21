'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_mpi_available\ntorch.distributed.is_mpi_available()\n'
import torch
input_data = torch.rand(100, 100)
print(torch.distributed.is_mpi_available())