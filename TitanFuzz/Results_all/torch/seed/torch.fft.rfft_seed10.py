input = torch.randn(4, 8)
output = torch.fft.rfft(input, n=None, dim=(- 1), norm=None, out=None)