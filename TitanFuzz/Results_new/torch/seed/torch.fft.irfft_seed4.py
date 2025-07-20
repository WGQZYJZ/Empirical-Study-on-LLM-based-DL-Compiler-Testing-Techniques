input = torch.randn(4, 4)
output = torch.fft.irfft(input, n=4, dim=(- 1), norm=None, out=None)