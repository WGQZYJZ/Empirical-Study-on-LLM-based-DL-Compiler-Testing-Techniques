input_data = torch.rand(1, 2, 3, 4)
output_data = torch.fft.rfft(input_data)
input_data = torch.rand(1, 2, 3, 4)
output_data = torch.fft.rfft2(input_data)