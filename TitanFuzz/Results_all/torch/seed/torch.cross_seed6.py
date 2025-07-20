input = torch.randn(4, 3)
other = torch.randn(4, 3)
torch.cross(input, other, dim=1)