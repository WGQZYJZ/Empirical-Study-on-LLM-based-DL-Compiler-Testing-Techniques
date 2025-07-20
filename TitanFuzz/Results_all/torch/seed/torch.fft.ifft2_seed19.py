(N, C, H, W) = (2, 3, 4, 4)
input = torch.randn(N, C, H, W)
output = torch.fft.ifft2(input, s=None, dim=((- 2), (- 1)), norm=None, out=None)