input = torch.randn(10, 4, 6)
glu = torch.nn.GLU(dim=(- 1))
output = glu(input)