input = torch.randn(3, requires_grad=True)
other = torch.randn(3, requires_grad=True)
res = torch.subtract(input, other)