input = torch.randn(10, 10)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)