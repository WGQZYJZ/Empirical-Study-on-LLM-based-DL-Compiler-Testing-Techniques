input = torch.randn(1, 1, 4, 4)
result = torch.fft.ifftn(input)