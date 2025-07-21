'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
rank = dist.get_rank()
world_size = dist.get_world_size()
tensor = torch.ones(1)
print(tensor)
dist.all_reduce(tensor)
print(tensor)