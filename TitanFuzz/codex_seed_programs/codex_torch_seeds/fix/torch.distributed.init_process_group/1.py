'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.init_process_group\n'
import torch
import torch.distributed as dist
tensor = torch.Tensor([1, 2, 3])
dist.init_process_group(backend='gloo', init_method='tcp://127.0.0.1:23456', rank=0, world_size=1)
dist.all_reduce(tensor, op=dist.reduce_op.SUM)
print(tensor)