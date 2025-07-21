'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.complex(a, b)
print('c:', c)
print('c.size():', c.size())
print('c.shape:', c.shape)
print('c.dtype:', c.dtype)
print('c.device:', c.device)
print('c.layout:', c.layout)
print('c.is_complex:', c.is_complex)
print('c.is_floating_point:', c.is_floating_point)
print('c.is_signed:', c.is_signed)