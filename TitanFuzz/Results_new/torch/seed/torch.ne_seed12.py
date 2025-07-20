input = torch.randn(3, requires_grad=True)
other = torch.randn(3)
output = torch.ne(input, other)