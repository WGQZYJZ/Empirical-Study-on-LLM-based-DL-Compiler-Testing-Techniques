input = torch.randn(8, 8, 4)
output = torch.fft.fftshift(input, dim=2)