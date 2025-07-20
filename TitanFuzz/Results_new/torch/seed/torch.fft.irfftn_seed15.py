input = torch.randn(1, 1, 3, 3, 3)
output = torch.fft.irfftn(input, s=None, dim=None, norm=None, out=None)