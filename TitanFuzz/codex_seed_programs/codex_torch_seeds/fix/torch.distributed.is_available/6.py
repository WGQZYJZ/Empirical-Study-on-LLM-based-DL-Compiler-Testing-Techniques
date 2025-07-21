'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_available\ntorch.distributed.is_available()\n'
import torch
import torch.distributed as dist
if True:
    print('PyTorch version:', torch.__version__)
    print('torch.distributed.is_available():', dist.is_available())