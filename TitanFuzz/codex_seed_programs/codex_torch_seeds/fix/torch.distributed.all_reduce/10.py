'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
tensor = torch.ones(2, 2)
dist.all_reduce(tensor, op=dist.reduce_op.SUM)
print(tensor)