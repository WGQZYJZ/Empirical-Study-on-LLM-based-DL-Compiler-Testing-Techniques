input = torch.randn(4, 5, 6, 7, 8)
output = torch.fft.fftn(input)