input = torch.randn(1, 2, 3, 4)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)