'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.complex\ntorch.complex(real, imag, *, out=None)\n'
import torch
real = torch.randn(1, 3, 4, 5)
imag = torch.randn(1, 3, 4, 5)
result = torch.complex(real, imag)
print(result)
print('Shape of result: ', result.shape)