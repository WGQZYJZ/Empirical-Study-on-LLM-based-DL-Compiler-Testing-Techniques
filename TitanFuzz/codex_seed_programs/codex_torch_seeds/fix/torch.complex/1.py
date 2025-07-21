'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.randn(3, 3)
imag = torch.randn(3, 3)
print(real)
print(imag)
print(torch.complex(real, imag))