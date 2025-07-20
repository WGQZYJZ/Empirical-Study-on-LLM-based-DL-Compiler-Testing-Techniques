input = torch.randn(1, 2, 4, 4)
output = torch.fft.irfft2(input)