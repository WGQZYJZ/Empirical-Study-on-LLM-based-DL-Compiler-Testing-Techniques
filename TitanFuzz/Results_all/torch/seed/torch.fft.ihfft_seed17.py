input_data = torch.randn(1, 2, 3, 4)
output_data = torch.fft.ihfft(input_data, n=None, dim=(- 1), norm=None, out=None)