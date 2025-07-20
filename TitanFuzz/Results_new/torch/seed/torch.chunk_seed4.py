input = torch.randn(4, 4)
output = torch.chunk(input, 2, dim=0)