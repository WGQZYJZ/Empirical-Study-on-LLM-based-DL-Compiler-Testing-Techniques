input_data = torch.randn(1, 1, 4)
output = torch.fft.ihfft(input_data)