input_data = torch.randn(2, 4, 8, dtype=torch.float32)
output = torch.fft.ifft(input_data)