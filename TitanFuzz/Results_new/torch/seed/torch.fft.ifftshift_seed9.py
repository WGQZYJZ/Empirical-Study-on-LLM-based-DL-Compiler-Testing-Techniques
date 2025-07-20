input = torch.randn(1, 2, 4, 4)
output = torch.fft.ifftshift(input, dim=None)