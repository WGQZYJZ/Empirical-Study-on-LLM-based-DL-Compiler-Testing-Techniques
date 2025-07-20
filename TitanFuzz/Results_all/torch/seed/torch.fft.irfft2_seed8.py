input = torch.randn(3, 3, 3)
output = torch.fft.irfft2(input)
input = torch.randn(3, 3, 3)
output = torch.fft.irfftn(input)