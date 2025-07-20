input = torch.randn(4, 8, 16, 32)
output = torch.fft.ifft(input, 3, 1)