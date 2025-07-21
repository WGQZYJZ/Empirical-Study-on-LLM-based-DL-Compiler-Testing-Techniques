'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.randn(1, 1)
imag = torch.randn(1, 1)
print('real: ', real)
print('imag: ', imag)
complex_tensor = torch.complex(real, imag)
print(complex_tensor)
print(complex_tensor.size())