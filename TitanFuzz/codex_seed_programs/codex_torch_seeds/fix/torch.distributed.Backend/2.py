'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.Backend\ntorch.distributed.Backend(name)\n'
import torch
data = torch.randn(4, 4)
torch.distributed.Backend('gloo')