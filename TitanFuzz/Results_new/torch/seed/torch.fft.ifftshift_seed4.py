input = torch.randn(8, 8)
output = torch.fft.ifftshift(input, dim=None)