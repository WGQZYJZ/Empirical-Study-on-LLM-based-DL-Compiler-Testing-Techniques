'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_initialized\ntorch.distributed.is_initialized()\n'
import torch
import torch
input_tensor = torch.randn(1, 1, 3, 3)
print(torch.distributed.is_initialized())