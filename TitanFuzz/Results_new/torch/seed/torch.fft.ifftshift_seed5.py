input = torch.randn(1, 5)
output = torch.fft.ifftshift(input, dim=None)