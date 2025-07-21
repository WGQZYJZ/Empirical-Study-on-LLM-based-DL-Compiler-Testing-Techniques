'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
c = torch.complex(a, b)
print(c)