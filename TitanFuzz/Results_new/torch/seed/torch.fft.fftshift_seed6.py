x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
y = torch.fft.fftshift(x, dim=0)