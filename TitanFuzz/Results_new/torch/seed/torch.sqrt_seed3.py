input = torch.randn(1, requires_grad=True)
output = torch.sqrt(input)
output.backward()