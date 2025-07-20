input = torch.randn(1, 2, 3, requires_grad=True)
other = torch.randn(1, 2, 3, requires_grad=True)
torch.special.xlogy(input, other)