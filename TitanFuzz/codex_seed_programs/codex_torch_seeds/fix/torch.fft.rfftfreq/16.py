'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftfreq\ntorch.fft.rfftfreq(n, d=1.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
t = torch.arange(0, 10, 0.01)
x = torch.sin(t)
freq = torch.fft.rfftfreq(len(t), d=0.01)
print(freq)
'\ntensor([0.0000e+00, 1.0000e-01, 2.0000e-01,  ..., 4.9990e+02, 4.9991e+02,\n        4.9992e+02])\n'