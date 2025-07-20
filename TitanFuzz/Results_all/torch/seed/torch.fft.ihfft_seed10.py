input = torch.randn(1, 2, 3, 2)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)