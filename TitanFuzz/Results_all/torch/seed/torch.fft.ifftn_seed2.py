input = torch.randn(2, 3, 4)
output = torch.fft.ifftn(input)