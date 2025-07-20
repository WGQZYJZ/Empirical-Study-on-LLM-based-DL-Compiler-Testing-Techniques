input = torch.randn(2, 3, 5)
dims = [1, 2, 0]
output = torch.permute(input, dims)