input_data = torch.randn(2, 3, 3, 3)
output = torch.fft.ifftn(input_data)