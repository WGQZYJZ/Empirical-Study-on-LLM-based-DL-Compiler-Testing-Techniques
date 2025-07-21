'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftfreq\ntorch.fft.fftfreq(n, d=1.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import numpy as np
N = 1024
T = (1.0 / 800.0)
x = np.linspace(0.0, (N * T), N)
y = (np.sin((((50.0 * 2.0) * np.pi) * x)) + (0.5 * np.sin((((80.0 * 2.0) * np.pi) * x))))
X = torch.tensor(y, dtype=torch.float32)
print(X.shape)
freq = torch.fft.fftfreq(N, d=T)
print(freq.shape)
X_fft = torch.fft.fft(X)
print(X_fft.shape)
X_fft_mag = torch.abs(X_fft)
print(X_fft_mag.shape)
X_fft_mag_db = (20 * torch.log10(X_fft_mag))