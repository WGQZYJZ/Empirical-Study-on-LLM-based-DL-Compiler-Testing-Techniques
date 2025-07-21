'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
if True:
    input_data = torch.randn(2, 3)
    dist.all_reduce(input_data, op=dist.reduce_op.SUM)
    print(input_data)