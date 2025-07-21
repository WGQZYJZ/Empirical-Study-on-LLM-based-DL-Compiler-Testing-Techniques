'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_nccl_available\ntorch.distributed.is_nccl_available()\n'
import torch
x = torch.Tensor([1, 2, 3])
y = torch.Tensor([4, 5, 6])
print(x)
print(y)
print(torch.distributed.is_nccl_available())