input = torch.randn(1, 2, 5, 5)
output = torch.fft.irfft2(input)
input = torch.randn(1, 2, 5, 5)
output = torch.fft.rfft(input)