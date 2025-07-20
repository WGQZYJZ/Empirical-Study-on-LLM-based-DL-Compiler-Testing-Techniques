input = torch.rand(2, 3, 4, 5, dtype=torch.float64)
out = torch.fft.rfft2(input)