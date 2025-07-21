'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
import torch.distributed as dist
print('PyTorch version: ', torch.__version__)
data = torch.randn(3, 2)
print('Input data: ', data)
if dist.is_initialized():
    print('PyTorch distributed package is initialized')
else:
    print('PyTorch distributed package is not initialized')