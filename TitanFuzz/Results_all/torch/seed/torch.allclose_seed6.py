input = torch.randn(2, 3, requires_grad=True)
other = torch.randn(2, 3, requires_grad=True)
output = torch.allclose(input, other)