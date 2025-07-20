input = torch.randn(8, 8, 8)
output = torch.fft.fftshift(input, dim=None)