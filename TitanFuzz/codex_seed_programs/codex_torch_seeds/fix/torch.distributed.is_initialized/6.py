'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
from torch.distributed import init_process_group
x = torch.randn(4, 4)
y = torch.randn(4, 4)
print(torch.distributed.is_initialized())