input = torch.randn(1, 1, 16, 16)
output = torch.fft.rfftn(input)