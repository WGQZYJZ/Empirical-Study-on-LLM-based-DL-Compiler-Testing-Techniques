input = torch.randn(1, 2, 3, 4, 5)
torch.fft.fftn(input)
torch.fft.ifftn(input)