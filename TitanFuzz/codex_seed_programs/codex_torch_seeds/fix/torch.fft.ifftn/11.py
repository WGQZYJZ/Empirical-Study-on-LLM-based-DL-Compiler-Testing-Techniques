'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftn\ntorch.fft.ifftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
from torch.autograd import gradcheck
input = torch.randn(4, 4, 4, dtype=torch.double, requires_grad=True)
input_np = np.random.randn(4, 4, 4)
print('input: ', input)
print('input_np: ', input_np)
print('\n\nTask 1: import PyTorch')
print('torch.__version__: ', torch.__version__)
print('torch.version.cuda: ', torch.version.cuda)
print('torch.backends.cudnn.version(): ', torch.backends.cudnn.version())
print('\n\nTask 2: Generate input data')
print('\n\nTask 3: Call the API torch.fft.ifftn')
output = torch.fft.ifftn(input)
print