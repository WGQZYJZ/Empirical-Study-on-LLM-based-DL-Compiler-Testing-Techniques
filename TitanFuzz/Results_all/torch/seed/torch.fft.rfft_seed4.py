input = torch.randn(1, 2, 8)
output = torch.fft.rfft(input, n=None, dim=(- 1), norm=None)