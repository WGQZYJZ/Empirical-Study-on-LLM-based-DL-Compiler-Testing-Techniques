input = torch.randn(1, 1, 4, 4)
output = torch.fft.rfft2(input)