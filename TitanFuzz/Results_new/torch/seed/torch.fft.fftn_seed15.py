input = torch.randn(2, 3, 4, 5)
output = torch.fft.fftn(input, s=None, dim=None, norm=None)