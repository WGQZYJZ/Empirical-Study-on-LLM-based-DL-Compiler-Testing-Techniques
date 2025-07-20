input_data = torch.randn(2, 3, 4)
output = torch.fft.fftn(input_data, norm=None)