input = torch.randn(1, requires_grad=True)
other = torch.randn(1, requires_grad=True)
output = torch.special.zeta(input, other)