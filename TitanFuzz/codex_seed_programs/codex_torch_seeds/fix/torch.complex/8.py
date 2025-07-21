'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.randn(2, 3)
imag = torch.randn(2, 3)
print(real)
print(imag)
complex_tensor = torch.complex(real, imag)
print(complex_tensor)
print(complex_tensor.real)
print(complex_tensor.imag)
print(complex_tensor.abs())