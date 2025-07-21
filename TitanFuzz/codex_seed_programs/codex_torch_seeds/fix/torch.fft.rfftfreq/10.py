'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftfreq\ntorch.fft.rfftfreq(n, d=1.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.arange(0, 3, 0.1)
print(x)
print(torch.fft.rfftfreq(x.size()[0], d=0.1))