input = torch.randn(2, 3)
chunks = torch.chunk(input, 2, dim=0)