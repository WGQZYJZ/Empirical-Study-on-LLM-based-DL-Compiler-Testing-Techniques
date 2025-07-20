input = torch.randn(1, requires_grad=True)
output = torch.arctan(input)
output.backward()