input = torch.randn(1, 4, 4)
output = torch.fft.fftshift(input, dim=None)