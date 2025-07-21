'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
import torch.distributed as dist
is_initialized = dist.is_initialized()
print('Initialized: ', is_initialized)