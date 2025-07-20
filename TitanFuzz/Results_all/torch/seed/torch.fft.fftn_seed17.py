input = torch.randn(4, 4)
output = torch.fft.fftn(input, dim=0)