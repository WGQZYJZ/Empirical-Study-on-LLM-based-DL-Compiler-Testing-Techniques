'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_available\ntorch.distributed.is_available()\n'
import torch
import torch.distributed as dist
data = torch.ones(1000, 1000)
if dist.is_available():
    print('Distributed package is available')
else:
    print('Distributed package is not available')