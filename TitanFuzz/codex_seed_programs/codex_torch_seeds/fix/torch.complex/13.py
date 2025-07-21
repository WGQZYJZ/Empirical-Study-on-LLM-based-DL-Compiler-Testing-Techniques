'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
print('Task 1: import PyTorch', torch.__version__)
real = torch.rand(4, 4)
imag = torch.rand(4, 4)
print('Task 3: Call the API torch.complex')
print(torch.complex(real, imag))