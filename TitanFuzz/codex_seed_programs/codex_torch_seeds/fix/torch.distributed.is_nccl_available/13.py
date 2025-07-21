'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_nccl_available\ntorch.distributed.is_nccl_available()\n'
import torch
input_data = torch.randn(2, 3, 3)
print('Input data: ', input_data)
print('Is NCCL available: ', torch.distributed.is_nccl_available())