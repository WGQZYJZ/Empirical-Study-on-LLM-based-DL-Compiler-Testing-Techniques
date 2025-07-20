input = torch.rand(2, 3, 4, 5, 6)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)