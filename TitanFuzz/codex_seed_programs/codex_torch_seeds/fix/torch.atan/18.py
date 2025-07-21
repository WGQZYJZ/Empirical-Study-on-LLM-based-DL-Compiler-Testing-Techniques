'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
if True:
    x = torch.randn(4)
    print('Input:', x)
    print('Output:', torch.atan(x))