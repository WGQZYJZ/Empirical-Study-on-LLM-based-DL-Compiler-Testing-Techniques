input_data = torch.randn(3, 4)
glu = torch.nn.GLU(dim=(- 1))
output = glu(input_data)