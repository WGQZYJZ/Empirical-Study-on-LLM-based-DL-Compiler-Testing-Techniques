input_data = torch.randn(2, 3, 4, 5)
result = torch.fft.ifft(input_data, n=None, dim=(- 1), norm=None, out=None)