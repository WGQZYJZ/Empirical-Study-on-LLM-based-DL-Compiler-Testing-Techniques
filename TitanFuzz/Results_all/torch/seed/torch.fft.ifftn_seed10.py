input = torch.randn(4, 4, 4)
output = torch.fft.ifftn(input)