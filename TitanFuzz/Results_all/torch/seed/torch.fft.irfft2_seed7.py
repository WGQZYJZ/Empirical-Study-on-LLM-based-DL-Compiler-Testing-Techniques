input_data = torch.randn(2, 5, 2, 3)
output_data = torch.fft.irfft2(input_data)