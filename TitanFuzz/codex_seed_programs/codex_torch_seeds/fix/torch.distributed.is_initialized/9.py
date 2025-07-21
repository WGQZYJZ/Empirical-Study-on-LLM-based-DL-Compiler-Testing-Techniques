'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
print('PyTorch version: ', torch.__version__)
a = torch.rand(10000, 10000)
b = torch.rand(10000, 10000)
print('torch.distributed.is_initialized() = ', torch.distributed.is_initialized())