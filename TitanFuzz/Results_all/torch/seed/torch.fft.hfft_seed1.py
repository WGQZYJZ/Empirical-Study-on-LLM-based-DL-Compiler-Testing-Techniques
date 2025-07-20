input = torch.randn(1, 2, 4, 2, dtype=torch.complex64)
output = torch.fft.hfft(input, n=None, dim=(- 1), norm=None)