'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_available\ntorch.distributed.is_available()\n'
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
print(torch.distributed.is_available())