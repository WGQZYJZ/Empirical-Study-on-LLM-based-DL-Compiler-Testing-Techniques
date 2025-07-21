'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_nccl_available\ntorch.distributed.is_nccl_available()\n'
import torch
import torch.distributed as dist
if True:
    print('PyTorch version: ', torch.__version__)
    print('Is NCCL available: ', dist.is_nccl_available())