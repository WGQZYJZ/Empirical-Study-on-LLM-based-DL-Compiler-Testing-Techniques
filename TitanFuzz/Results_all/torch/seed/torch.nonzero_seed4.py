input = torch.randn(3, 4)
indices = torch.nonzero(input)
indices = torch.nonzero(input, as_tuple=True)