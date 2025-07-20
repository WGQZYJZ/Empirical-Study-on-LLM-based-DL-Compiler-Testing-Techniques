input = torch.randn(2, 3, 4, 5, 6)
output = torch.fft.fft2(input, s=None, dim=((- 2), (- 1)), norm=None, out=None)