input = torch.randn(1, 1, 8, 8)
output = torch.fft.fft2(input)
output = torch.fft.ifft2(input)