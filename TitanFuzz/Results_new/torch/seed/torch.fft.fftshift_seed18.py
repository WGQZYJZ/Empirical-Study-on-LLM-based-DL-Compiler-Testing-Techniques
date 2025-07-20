input = torch.randn(2, 3, 4, 5)
output = torch.fft.fftshift(input, dim=2)