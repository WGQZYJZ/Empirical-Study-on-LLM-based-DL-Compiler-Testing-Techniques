'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
input_tensor = torch.rand(1, 1, requires_grad=True)
dist.all_reduce(input_tensor)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
input_tensor = torch.rand(1, 1, requires_grad=True)
dist.all_reduce(input_tensor)
print(input_tensor)