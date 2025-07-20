input = torch.randn(4, 4, 8)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)