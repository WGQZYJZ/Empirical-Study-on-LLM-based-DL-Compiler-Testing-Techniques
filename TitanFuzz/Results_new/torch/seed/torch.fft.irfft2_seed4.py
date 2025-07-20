input = torch.randn(3, 4, 5)
s = None
dim = ((- 2), (- 1))
norm = None
output = torch.fft.irfft2(input, s, dim, norm)