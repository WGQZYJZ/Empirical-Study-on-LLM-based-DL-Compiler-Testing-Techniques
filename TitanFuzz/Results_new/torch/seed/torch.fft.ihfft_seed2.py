input = torch.randn(4, 1, 8)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)