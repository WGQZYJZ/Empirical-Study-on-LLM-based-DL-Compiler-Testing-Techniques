'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftn\ntorch.fft.ifftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
if True:
    print('Task 1: import PyTorch')
    print('PyTorch version: ', torch.__version__)
    print('CUDA available: ', torch.cuda.is_available())
    print('cuDNN enabled: ', torch.backends.cudnn.enabled)
    print('')
    print('Task 2: Generate input data')
    input = torch.randn(4, 4, 4, dtype=torch.float32, device='cuda')
    print('Input: ', input)
    print('')
    print('Task 3: Call the API torch.fft.ifftn')
    output = torch.fft.ifftn(input, norm=None)
    print('Output: ', output)
    print('')