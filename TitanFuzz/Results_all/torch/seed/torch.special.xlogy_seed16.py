input = torch.randn(2, 3, requires_grad=True)
other = torch.randn(2, 3, requires_grad=True)
xlogy = torch.special.xlogy(input, other)
xlogy.backward(torch.ones(2, 3))