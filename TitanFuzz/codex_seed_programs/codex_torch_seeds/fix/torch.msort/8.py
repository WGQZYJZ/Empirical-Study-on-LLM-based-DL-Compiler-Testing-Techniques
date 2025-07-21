'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
if True:
    print('PyTorch version:', torch.__version__)
    x = torch.randn(3, 4)
    print('Input data x:', x)
    y = torch.msort(x)
    print('Output data y:', y)