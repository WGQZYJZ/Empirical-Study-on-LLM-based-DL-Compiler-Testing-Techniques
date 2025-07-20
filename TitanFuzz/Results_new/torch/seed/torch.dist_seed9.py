input = torch.randn(3, 5, requires_grad=True)
other = torch.randn(3, 5)
result = torch.dist(input, other, p=2)
result = torch.dist(input, other, p=1)