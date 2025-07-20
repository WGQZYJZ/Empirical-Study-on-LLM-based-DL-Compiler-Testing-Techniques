input = torch.randn(1, 1, 5, 5)
output = torch.fft.ifft2(input)