'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.randn(2, 3, 4)
imag = torch.randn(2, 3, 4)
complex = torch.complex(real, imag)
print('complex = ', complex)