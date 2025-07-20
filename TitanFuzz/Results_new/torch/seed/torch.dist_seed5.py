input = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.dist(input, other, p=2)