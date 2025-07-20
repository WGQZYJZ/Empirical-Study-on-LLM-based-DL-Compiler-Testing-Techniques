input = torch.randn(3, 8, 5, dtype=torch.float)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)