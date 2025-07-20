input_data = torch.rand(2, 3, 4)
output_data = torch.fft.fftshift(input_data, dim=None)