input = torch.randn(1, 2, 3, 4, 5)
output = torch.fft.irfftn(input, s=None, dim=None, norm=None, out=None)