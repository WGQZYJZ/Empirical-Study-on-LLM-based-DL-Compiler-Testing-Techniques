x = torch.randn(1, 2, 3, 4, 5)
y = torch.fft.rfft(x, n=None, dim=(- 1), norm=None, out=None)