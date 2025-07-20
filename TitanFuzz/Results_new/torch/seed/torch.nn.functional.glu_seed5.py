input = torch.randn(3, 4)
output = torch.nn.functional.glu(input, dim=(- 1))