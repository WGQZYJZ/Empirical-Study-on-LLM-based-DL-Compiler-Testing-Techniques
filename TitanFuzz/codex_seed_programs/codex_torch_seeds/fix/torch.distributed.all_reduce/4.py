'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.all_reduce\n'
import torch
import torch.distributed as dist
if True:
    print('PyTorch version:', torch.__version__)
    print('Is CUDA available:', torch.cuda.is_available())
    x = torch.randn(1, requires_grad=True)
    print('x:', x)
    dist.all_reduce(x, op=dist.ReduceOp.SUM)
    print('x after all_reduce:', x)