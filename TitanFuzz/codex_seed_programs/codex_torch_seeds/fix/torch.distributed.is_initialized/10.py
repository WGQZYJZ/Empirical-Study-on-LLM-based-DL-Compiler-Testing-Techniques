'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
import torch.distributed as dist
input_data = torch.randn(10)
if dist.is_initialized():
    print('Distributed is initialized')
else:
    print('Distributed is not initialized')