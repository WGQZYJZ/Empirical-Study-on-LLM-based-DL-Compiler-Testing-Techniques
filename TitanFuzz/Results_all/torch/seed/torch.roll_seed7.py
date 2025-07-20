input = torch.randn(3, 4, 5)
output = torch.roll(input, shifts=2, dims=2)