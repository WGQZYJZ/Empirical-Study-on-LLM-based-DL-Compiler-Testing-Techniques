'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real_data = torch.randn(2, 3)
imag_data = torch.randn(2, 3)
complex_data = torch.complex(real_data, imag_data)
print(complex_data)