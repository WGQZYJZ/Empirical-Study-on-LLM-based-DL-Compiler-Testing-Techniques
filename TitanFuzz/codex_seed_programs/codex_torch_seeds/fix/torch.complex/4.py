'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
print('Input data:')
real = torch.randn(4, 4)
imag = torch.randn(4, 4)
print('real:', real)
print('imag:', imag)
print('\nOutput data:')
out = torch.complex(real, imag)
print('out:', out)