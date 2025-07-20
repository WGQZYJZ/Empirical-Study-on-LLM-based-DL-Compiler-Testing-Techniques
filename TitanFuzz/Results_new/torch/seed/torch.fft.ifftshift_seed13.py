input_data = torch.arange(1, 17).view(4, 4)
output_data = torch.fft.ifftshift(input_data)