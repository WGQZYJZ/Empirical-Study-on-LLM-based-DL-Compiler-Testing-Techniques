'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.FileStore\ntorch.distributed.FileStore()\n'
import torch
import torch.distributed as dist
if True:
    print('PyTorch version: {}'.format(torch.__version__))
    input_tensor = torch.randn(4, 3)
    print('Input tensor: {}'.format(input_tensor))
    dist.FileStore('./')