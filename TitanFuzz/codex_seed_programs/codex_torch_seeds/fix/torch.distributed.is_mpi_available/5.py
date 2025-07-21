'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_mpi_available\ntorch.distributed.is_mpi_available()\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
y = torch.tensor([1.0, 3.0, 2.0, 4.0, 5.0, 7.0, 6.0, 8.0, 9.0, 10.0])
print(torch.distributed.is_mpi_available())