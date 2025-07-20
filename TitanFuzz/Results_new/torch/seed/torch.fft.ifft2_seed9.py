input = torch.randn(1, 2, 3, 4, 5)
output = torch.fft.ifft2(input)