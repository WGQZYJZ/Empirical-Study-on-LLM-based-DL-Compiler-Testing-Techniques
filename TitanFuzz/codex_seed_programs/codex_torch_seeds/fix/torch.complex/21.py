'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.rand(5, 3)
imag = torch.rand(5, 3)
out = torch.complex(real, imag)
print(out)