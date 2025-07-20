input = torch.randn(4, 8, 32)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)