input = torch.randn(4, 3)
other = torch.randn(4, 3)
output = torch.cross(input, other, dim=1)