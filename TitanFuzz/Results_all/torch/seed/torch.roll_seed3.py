input = torch.randn(2, 3, 4)
output = torch.roll(input, shifts=2, dims=1)