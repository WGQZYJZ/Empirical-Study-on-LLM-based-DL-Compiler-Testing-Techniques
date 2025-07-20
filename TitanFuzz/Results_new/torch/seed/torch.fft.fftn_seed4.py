input = torch.randn(1, 2, 2, 2, 2)
input = torch.tensor(input, dtype=torch.float32)
output = torch.fft.fftn(input)