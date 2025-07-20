input_data = torch.randn(4, 4, 4)
result = torch.fft.ihfft(input_data, n=None, dim=(- 1), norm=None, out=None)