data = torch.randn(1, 1, 4, 4)
output = torch.nn.functional.interpolate(data, size=(8, 8))