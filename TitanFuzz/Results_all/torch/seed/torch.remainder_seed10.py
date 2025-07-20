input = torch.randn(3, 3, requires_grad=True)
other = torch.randn(3, 3, requires_grad=True)
output = torch.remainder(input, other)