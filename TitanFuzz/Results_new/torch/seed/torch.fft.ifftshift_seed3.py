input_data = torch.randn(3, 4, 5)
output = torch.fft.ifftshift(input_data, dim=None)