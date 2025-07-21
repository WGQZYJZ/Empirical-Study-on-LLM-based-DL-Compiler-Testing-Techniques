'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input = torch.randn(8, 8)
out = torch.fft.rfft(input)
print(out)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input = torch.randn(8, 8)
out = torch.fft.irfft(input)
print(out)