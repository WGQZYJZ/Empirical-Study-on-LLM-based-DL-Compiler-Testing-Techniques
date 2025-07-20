input_data = torch.randn(10, 10, 10)
output_data = torch.fft.ihfft(input_data, n=None, dim=(- 1), norm=None, out=None)