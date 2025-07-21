'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
import torch
import torch.distributed as dist
tensor = torch.Tensor([1, 2, 3])
dist.all_reduce(tensor, op=dist.reduce_op.SUM)
print(tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
import torch
import torch.distributed as dist
tensor = torch.Tensor([1, 2, 3])
dist.all_reduce(tensor, op=dist.reduce_op.SUM)
print(tensor)