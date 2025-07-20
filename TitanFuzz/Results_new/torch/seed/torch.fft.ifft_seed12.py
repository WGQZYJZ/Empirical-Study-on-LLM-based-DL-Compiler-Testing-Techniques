input_data = torch.randn(2, 3, 4, 5)
output_data = torch.fft.ifft(input_data)