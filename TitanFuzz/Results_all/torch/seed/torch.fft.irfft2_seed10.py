input = torch.randn(4, 8, 8)
output = torch.fft.irfft2(input)