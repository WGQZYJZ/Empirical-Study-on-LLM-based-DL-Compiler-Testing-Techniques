input = torch.randn(3, 4)
output = torch.nn.functional.softmin(input, dim=0)