input = torch.randn(3, 4, 5)
output = torch.fft.irfft2(input)