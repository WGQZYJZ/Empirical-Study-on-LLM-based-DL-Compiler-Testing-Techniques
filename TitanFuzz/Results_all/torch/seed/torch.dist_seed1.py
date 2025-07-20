input = torch.randn(3, requires_grad=True)
other = torch.randn(3)
torch.dist(input, other, p=2)