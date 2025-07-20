input = torch.randn(1, 1, 8, 8, requires_grad=True)
output = torch.fft.fft2(input)